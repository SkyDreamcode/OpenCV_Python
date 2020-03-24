#!/usr/bin/python
import picamera
import time
import numpy as np
import cv2

def record_video_by_picamera():
    camera = picamera.PiCamera()
    camera.resolution = (460, 480)
    camera.start_recording('video_test.h264')
    camera.wait_recording(20)
    camera.stop_recording()

#due to picamera output data is the format of RGB,so need ttransform to BGR format by Numpy
def RGB_to_BGR_by_Numpy():
    camera.resolution = (320, 240)
    camera.framerate = 30
    time.sleep(2)
    imag = np.empty((240 * 320 * 3,), dtype=np.uint8)
    #save as bgr for opencv
    camera.capture(imag, 'bgr')
    imag = imag.reshape(240,320,3)
    cv2.imshow('img', image)
    if(cv2.waitKey(0) == ord('q')):
        print('rgb_to_bgr is exit')
        exit(0)

def python_opencv_test():
    print("OpenCV Version:{}".format(cv2.__version__))
    # 0: use CSI camera,1：use USB camera
    cap = cv2.VideoCapture(0)
    if(not cap.isOpened()):
        print("can't open this camera")

    while(True):
        ret, FrameImage = cap.read()
        if ret == True:
            # change to gray image
            GrayImage = cv2.cvtColor(FrameImage, cv2.COLOR_BGR2GRAY)
            # blur the image 
            BlurImage = cv2.blur(GrayImage,(7,7))
            # use canny to detect contour
            CannyImage = cv2.Canny(BlurImage,3,9)
            # show the image
            cv2.imshow('Camera Capture',CannyImage)
            #Press Q to quit
            if (cv2.waitKey(1)) == ord('q'):
                cap.release()
                break
        else:
            break


def camera_preview():
    with picamera.PiCamera() as camera:
        camera.resolution = (480, 800)
        camera.framerate = 30
        print('start preview direct from gpu')
        camera.start_preview()# the start_preview function
        time.sleep(1000)
        print('end preview')

