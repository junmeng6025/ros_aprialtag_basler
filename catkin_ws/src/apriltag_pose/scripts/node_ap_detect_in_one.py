#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float32MultiArray, MultiArrayDimension
from geometry_msgs.msg import Pose, PoseArray
import tf.transformations as tr
from cv_bridge import CvBridge

from pypylon import pylon
import cv2
import apriltag
from apriltag import *
from argparse import ArgumentParser
from pathlib import Path
import time
from basler_detect import ApriltagDetector, BaslerPublisher
import os
from apriltag_pose.msg import Poses


QUEUE_SIZE = 10
FPS = 30
# IMGSAVE_DIR = os.path.join(os.getcwd(), '../saved_img')


def publish_img(img_pub, bridge, image):
    """
    publish image messages\n
    INPUT:
        img_pub:    a rospy.Publisher                           type: Image
        bridge:     an obj of CvBridge()
        image:      image data, converted from .png             type: np.array
    OUTPUT:
        void
    """
    img_pub.publish(bridge.cv2_to_imgmsg(image, "bgr8"))


def publish_poses(pose_pub, poses_msg):
    pose_pub.publish(poses_msg)


def cvt_posemat2quaternion(pose_mat):
    rmat = pose_mat[:3, :3]
    tvec = pose_mat[:3, 3]
    quat = tr.quaternion_from_matrix(pose_mat)

    pose_msg = Pose()
    pose_msg.position.x = tvec[0]
    pose_msg.position.y = tvec[1]
    pose_msg.position.z = tvec[2]
    pose_msg.orientation.x = quat[0]
    pose_msg.orientation.y = quat[1]
    pose_msg.orientation.z = quat[2]
    pose_msg.orientation.w = quat[3]

    return pose_msg


def init_posearray():
    pose_array = PoseArray()
    pose_array.header.frame_id = "map"
    pose_array.header.stamp = rospy.Time.now()
    return pose_array


if __name__ == '__main__':
    # Initialize BASLER camera connector & AprilTag detector
    basler_publisher = BaslerPublisher()
    detector = ApriltagDetector()
    # ROOT = str(Path.cwd())
    # saved_dir = ROOT + "/saved_img"

    # Initialize ROS node and Publishers
    rospy.init_node('node_ap_detect', anonymous=True)
    frame = 0
    img_raw_pub = rospy.Publisher('im_raw', Image, queue_size=QUEUE_SIZE)
    img_detect_pub = rospy.Publisher('im_detect', Image, queue_size=QUEUE_SIZE)
    pose_pub = rospy.Publisher('poses', Poses, queue_size=QUEUE_SIZE)

    bridge = CvBridge()
    rate = rospy.Rate(FPS)
    poses_msg = Poses()
    poses_msg.pose_array = init_posearray()

    # k = 0

    # BASLER camera image incoming
    basler_publisher.start()

    # Start ROS cycle
    if basler_publisher.is_start:
        while not rospy.is_shutdown():
            is_grabed = basler_publisher.img_grabbing()
            if is_grabed:
                publish_img(img_raw_pub, bridge, basler_publisher.raw_img)

                poses, result, img_detected = detector.detect(
                    basler_publisher.raw_img)
                publish_img(img_detect_pub, bridge, img_detected)

                if len(poses) == 0:
                    rospy.logwarn("[WARNING] No AptilTag detected...")
                else:
                    for i, pose in enumerate(poses):
                        pose_msg = cvt_posemat2quaternion(pose)
                        poses_msg.ids.append(i)
                        poses_msg.pose_array.poses.append(pose_msg)

                publish_poses(pose_pub, poses_msg)

                # k = cv2.waitKey(1)
                # if k == 32:
                #     basler_publisher.save_imgcapture(IMGSAVE_DIR)
                #     rospy.loginfo("##################### img %05d saved to %s #####################"
                #                   % (basler_publisher.capture_counter, IMGSAVE_DIR))
                # if k == 120:
                #     break
            else:
                rospy.logwarn("[WARNING] Cannot receive image frame")
                continue
            rospy.loginfo('Frame[%010d]: published' % frame)
            rate.sleep()
            frame += 1

        basler_publisher.stop()
    else:
        rospy.logerr("[ERROR] Failed to launch the camera.")
