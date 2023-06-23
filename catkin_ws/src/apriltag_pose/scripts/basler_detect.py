'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2
import apriltag
from apriltag import *
from argparse import ArgumentParser
from pathlib import Path
import time


class ApriltagDetector():
    def __init__(self):
        parser = ArgumentParser(
            description='Detect AprilTags from video stream.')
        apriltag.add_arguments(parser)
        # options = parser.parse_args()
        options, _ = parser.parse_known_args()
        # -> prevent failing due to arguments added automatically by roslaunch.
        self.detector = apriltag.Detector(
            options, searchpath=apriltag._get_dll_path())

    def detect(self, img_raw):
        img_copy = img_raw.copy()
        poses, result, overlay = apriltag.detect_tags(
            img_copy,
            self.detector,
            camera_params=(3156.71852, 3129.52243, 359.097908, 239.736909),
            tag_size=0.0762,
            vizualization=3,
            verbose=3,
            annotation=True)
        '''
        Detect AprilTags from image.

        Args:   image [image]: Input image to run detection algorithm on
                detector [detector]: AprilTag Detector object
                camera_params [_camera_params]: Intrinsic parameters for camera (fx, fy, cx, cy)
                tag_size [float]: Physical size of tag in user defined units (m or mm recommended)
                vizualization [int]: 0 - Highlight
                                    1 - Highlight + Boxes
                                    2 - Highlight + Axes
                                    3 - Highlight + Boxes + Axes
                verbose [int]: 0 - Silent
                            1 - Number of detections
                            2 - Detection data
                            3 - Detection and pose data
                annotation [bool]: Render annotated text on detection window
        '''
        return poses, result, overlay


class BaslerPublisher():
    def __init__(self):
        self.camera = pylon.InstantCamera(
            pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        self.frame_counter = 0
        self.capture_counter = 0
        self.is_start = False
        self.grabResult = None
        self.init_time = time.time()

    def start(self):
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.is_start = self.camera.IsGrabbing()

    def set_grabResult(self, grabResult):
        self.grabResult = grabResult

    def img_grabbing(self):
        grabResult = self.camera.RetrieveResult(
            5000, pylon.TimeoutHandling_ThrowException)
        self.set_grabResult(grabResult)

        if self.grabResult.GrabSucceeded():
            image = self.converter.Convert(self.grabResult)
            # self.set_rawImg(image.GetArray())
            self.raw_img = image.GetArray()
            # cv2.namedWindow('basler capture', cv2.WINDOW_NORMAL)
            # cv2.imshow('basler capture', img)
            # self.fps = self.camera.ResultingFrameRateAbs.GetValue()
            time_span = time.time() - self.init_time
            print(
                "[INFO] Grabbing video frame [#%06d] @ fps %f" % (self.frame_counter, self.frame_counter/time_span))
            self.frame_counter += 1

            return True
        else:
            print("[ERROR] Cannot receive frame (stream end?)")
            return False

    def save_imgcapture(self, path):
        cv2.imwrite(
            path+"/snapshot_%05d.bmp" % self.capture_counter, self.raw_img)
        print(
            "##################### img %05d saved to %s #####################" % (self.capture_counter, path))
        self.capture_counter += 1

    def stop(self):
        self.grabResult.Release()
        self.camera.StopGrabbing()


if __name__ == '__main__':
    basler_publisher = BaslerPublisher()
    detector = ApriltagDetector()
    ROOT = str(Path.cwd())
    saved_dir = ROOT + "/saved_img"

    basler_publisher.start()
    cv2.namedWindow("AprilTag detected", cv2.WINDOW_NORMAL)
    if basler_publisher.is_start:
        while True:
            is_grabed = basler_publisher.img_grabbing()
            if is_grabed:
                poses, result, img_detected = detector.detect(
                    basler_publisher.raw_img)
                cv2.imshow("AprilTag detected", img_detected)
                k = cv2.waitKey(1)
                if k == 32:
                    basler_publisher.save_imgcapture(saved_dir)
                if k == 120:
                    break
            else:
                print("[WARNING] Cannot receive image frame")
                continue
        basler_publisher.stop()
    else:
        print("[ERROR] Failed to launch the camera.")

    cv2.destroyAllWindows()
