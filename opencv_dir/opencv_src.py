#coding:utf-8
import cv2

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

