#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge


QUEUE_SIZE = 1
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


def publish_frame(frame_pub, frame):
    frame_msg = Int32()
    frame_msg.data = frame
    frame_pub.publish(frame_msg)


if __name__ == '__main__':
    # Get image using opencv
    cap = cv2.VideoCapture(0)
    # id = 0: Webcam
    # id = 2: SONY camera

    # Initialize ROS node and Publishers
    rospy.init_node('node_webcam_imgpub', anonymous=True)
    frame = 0
    img_raw_pub = rospy.Publisher('img_raw', Image, queue_size=QUEUE_SIZE)
    frame_pub = rospy.Publisher('frame', Int32, queue_size=QUEUE_SIZE)

    bridge = CvBridge()
    rate = rospy.Rate(FPS)

    # Start ROS cycle
    if cap.isOpened():
        while not rospy.is_shutdown():
            ret, cvImg = cap.read()
            if ret:
                publish_img(img_raw_pub, bridge, cvImg)
            else:
                rospy.logwarn("Cannot receive image frame")
                continue
            # rospy.loginfo('Frame[%010d]: published' % frame)
            rate.sleep()
            frame += 1
            publish_frame(frame_pub, frame)
            rospy.loginfo('Frame[%010d]: published' % frame)
    else:
        rospy.logerr("Failed to launch the camera.")
