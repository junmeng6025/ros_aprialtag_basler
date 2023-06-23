#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from geometry_msgs.msg import Pose, PoseArray
import tf.transformations as tr
from cv_bridge import CvBridge

from basler_detect import ApriltagDetector, BaslerPublisher
from apriltag_pose.msg import Poses
import argparse


QUEUE_SIZE = 1
FPS = 30


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


class PosePublisher(object):
    def __init__(self):
        self.bridge = CvBridge()
        self.rate = rospy.Rate(FPS)
        self.poses = None
        self.detector = ApriltagDetector()
        self.poses_msg = Poses()
        self.poses_msg.pose_array = init_posearray()

        # Subscriber
        rospy.Subscriber("/frame", Int32, self.frameCallback)
        rospy.Subscriber("/img_raw", Image, self.imBaslerCallback)

        # Publisher
        self.pose_pub = rospy.Publisher('poses', Poses, queue_size=QUEUE_SIZE)
        self.img_detect_pub = rospy.Publisher(
            'im_detect', Image, queue_size=QUEUE_SIZE)

    def frameCallback(self, frame_msg):
        rospy.loginfo('Frame[%010d]: subscribed' % frame_msg.data)

    def imBaslerCallback(self, img_data):
        cvImage = self.bridge.imgmsg_to_cv2(img_data, "bgr8")
        self.poses, result, img_detected = self.detector.detect(cvImage)
        publish_img(self.img_detect_pub, self.bridge, img_detected)

    def start(self):
        rospy.loginfo("Starting...")
        while not rospy.is_shutdown():

            if self.poses is None:
                rospy.logwarn("No AptilTag detected...")
            else:
                for i, pose in enumerate(self.poses):
                    pose_msg = cvt_posemat2quaternion(pose)
                    self.poses_msg.ids.append(i)
                    self.poses_msg.pose_array.poses.append(pose_msg)

            publish_poses(self.pose_pub, self.poses_msg)
            self.rate.sleep()


if __name__ == '__main__':

    # parser = argparse.ArgumentParser()
    # parser.parse_args()
    # Initialize ROS node
    rospy.init_node('node_posepub', anonymous=True)
    pose_pub = PosePublisher()
    pose_pub.start()
