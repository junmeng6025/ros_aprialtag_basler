#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


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
