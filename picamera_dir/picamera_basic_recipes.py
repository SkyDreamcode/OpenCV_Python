#coding:utf-8
from time import sleep
from picamera import PiCamera
from io import BytesIO
from PIL import Image

def capturing_consistent_images():
    camera = PiCamera(resolution=(480, 480), framerate = 30)
    camera.iso = 100
    sleep(2)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode='off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.capture_sequence(['imge%d.jpg' % i for i in range(10)])



def capturing_resize_image():
    camera = PiCamera();
    camera.resolution = (640,480)
    camera.start_preview()
    sleep(4)
    camera.capture('2nd.jpg', resize=(320,240))

def capturing_to_a_PIL_image():
    stream = BytesIO()
    camera = PiCamera()
    camera.start_preview();
    sleep(5)
    camera.capture(stream, format='jepg')
    stream.seek(0)
    image = Image.open(stream)


def capturing_to_a_file():
    #with PiCamera as camera:
    camera = PiCamera()
    camera.resolution = (240, 480)
    camera.start_preview()
    sleep(5)#camera warm-up time
    camera.capture('capture_file.jpg')

def capturing_to_a_stream():
    '''
    my_stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture(my_stream, 'jpeg')
    '''
    my_file = open('my.jpg', 'wb')
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture(my_file)
    my_file.close()
