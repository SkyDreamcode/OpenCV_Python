#coding:utf-8
import cv2
import numpy as np

def ROI_test():
    img = cv2.imread('capture_file.jpg')
    
    #create a window
    cv2.namedWindow('image', flags = cv2.WINDOW_NORMAL|cv2.WINDOW_FREERATIO)
    cv2.namedWindow('image_rio', flags = cv2.WINDOW_NORMAL|cv2.WINDOW_FREERATIO)

    cv2.imshow('image',img)

    showCrosshair = True

    fromCenter = False
    #attribute：‘module’object has no attribute ‘selectROI’
    rect = cv2.selectROI('image', img, showCrosshair, fromCenter)

    (x, y, w, h) = rect

    imcrop = img[y: y+h, x:x+w]

    cv2.imshow('image_roi', imcrop)

    cv2.imwrite('image_rio.png', imcrop)
    cv2.waitKey(0)

def paint_test():
    COLOR_MAP={
        "blue":(255,0,0),
        "green":(0,255,0),
        "red":(0,0,255),
        "white":(255,255,255)
    }

    def InitPaint(width, height, color=COLOR_MAP['white']):
        paint= np.ones((height, width, 3), dtype='uint8')
        paint[:] = color
        return paint

    paint = InitPaint(600, 600)

    cv2.line(paint, pt1=(0,0),pt2=(600,600), color=COLOR_MAP["red"])

    cv2.circle(paint, center=(150, 150), radius=50, color=COLOR_MAP["green"])

    cv2.circle(paint, (150, 150), 30, color=COLOR_MAP["blue"], thickness=-1)

    cv2.rectangle(paint, (10, 10), (60, 60), COLOR_MAP['red'])

    points = np.array([[100,50],[200,200],[270,200],[290,100]], np.int32)

    points = points.reshape((-1,1,2))

    cv2.polylines(paint, pts=[points], isClosed=True, color=COLOR_MAP["red"], thickness=3)

    cv2.ellipse(img=paint,center=(256,256), axes=(40,20), angle=0, startAngle=0, endAngle=360, color=(100, 200, 0), thickness=-1)

    font = cv2.FONT_HERSHEY_SIMPLEX

    line = cv2.LINE_AA

    cv2.putText(img=paint, text="Hello", org=(10, 250), fontFace=font, fontScale=2, color=(0, 0, 255),thickness=1, lineType=line)

    cv2.imshow('Paint', paint)

    cv2.waitKey(0)

def camera_save_to_local():
    #set for camera
    capCamera = cv2.VideoCapture(0)
    capCamera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    capCamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    print('fourcc %s' %fourcc)
    fps = 30
    print('fps:%d' %fps)
    framesize = (int(capCamera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capCamera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(framesize)

    outCamera = cv2.VideoWriter('outputCamera.avi', fourcc, fps, framesize)


    while(capCamera.isOpened()):
        ret , frameCamera = capCamera.read()
        outCamera.write(frameCamera)
        cv2.imshow('outputCamera', frameCamera)
        if(cv2.waitKey(1) == ord('q')):
            break

    capCamera.release()
    cv2.destroyAllWindows()

def read_save_video():
    capVideo = cv2.VideoCapture('outputCamera.avi')

    fourcc = int(capVideo.get(cv2.CAP_PROP_FOURCC))
    print('fourcc=',fourcc)
    fps = capVideo.get(cv2.CAP_PROP_FPS)
    print('fps=%d'%fps)
    frameSize=(int(capVideo.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('frameSize=', frameSize)
    outVideo = cv2.VideoWriter("outputVideo", fourcc, fps, frameSize)
    while(capVideo.isOpened()):
        ret, frameVideo = capVideo.read()
        if ret:
            outVideo.write(frameVideo)
            cv2.imshow('framvideo', frameVideo)
        if cv2.waitKey(1) == ord('q'):
            break

    capVideo.release()
    cv2.destroyAllWindows()

def camera_video_show():
    capcamera = cv2.VideoCapture(0)
    if(not capcamera.isOpened()):
        print('cant open this camera')
        exit(0)
    capcamera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    capcamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

    flipcode = 1

    while(True):
        ret, framecamera= capcamera.read()
        framecamera = cv2.flip(framecamera, flipcode)
        if ret == True:
            cv2.imshow('camera', framecamera)
        else:
            break

        if(cv2.waitKey(1) == ord('q')):
            break


def get_pixel_value():
    img = cv2.imread("capture_file.jpg")
    cv2.imshow('image', img)
    print(img[100:102, 100:102])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def image_display_output():
    img1 = cv2.imread("capture_file.jpg")
    cv2.imshow('img1', img1)
    cv2.imwrite('img11.jpg', img1)

    img2 = cv2.imread("capture_file.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img2', img2)
    cv2.imwrite('img22.jpg', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

