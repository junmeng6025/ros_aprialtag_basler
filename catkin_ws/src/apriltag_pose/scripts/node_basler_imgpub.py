#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge
from basler_detect import BaslerPublisher


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
    # Initialize BASLER camera connector & AprilTag detector
    basler_publisher = BaslerPublisher()

    # Initialize ROS node and Publishers
    rospy.init_node('node_basler_imgpub', anonymous=True)
    frame = 0
    img_raw_pub = rospy.Publisher('img_raw', Image, queue_size=QUEUE_SIZE)
    frame_pub = rospy.Publisher('frame', Int32, queue_size=QUEUE_SIZE)

    bridge = CvBridge()
    rate = rospy.Rate(FPS)

    # BASLER camera image incoming
    basler_publisher.start()

    # Start ROS cycle
    if basler_publisher.is_start:
        while not rospy.is_shutdown():
            is_grabed = basler_publisher.img_grabbing()
            if is_grabed:
                publish_img(img_raw_pub, bridge, basler_publisher.raw_img)
            else:
                rospy.logwarn("Cannot receive image frame")
                continue
            # rospy.loginfo('Frame[%010d]: published' % frame)
            rate.sleep()
            frame += 1
            publish_frame(frame_pub, frame)
            rospy.loginfo('Frame[%010d]: published' % frame)

        basler_publisher.stop()
    else:
        rospy.logerr("Failed to launch the camera.")
