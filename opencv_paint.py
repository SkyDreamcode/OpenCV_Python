#coding:utf-8
import cv2  
import numpy as np  

# 判断鼠标是否按下的标志
isMouseLBDown = False
# 画笔的颜色
circleColor = (0, 0, 0)
# 画笔的粗壮
circleRadius = 5
# 上一次的点
lastPoint = (0, 0)

# 定义鼠标函数，用于绘图
def draw_circle(event,x,y,flags,param): 

    global img
    global isMouseLBDown
    global color
    global lastPoint

    if event == cv2.EVENT_LBUTTONDOWN:
        # 检测到鼠标左键按下，按下就画圆，并且记录抬起按键之前的点
        isMouseLBDown = True
        cv2.circle(img,(x,y), int(circleRadius/2), circleColor,-1)
        lastPoint = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        # 检测到鼠标左键抬起
        isMouseLBDown = False
    elif event == cv2.EVENT_MOUSEMOVE:
        # 如果鼠标左键按下，并且鼠标在移动,就画线
        # 并且记录按键抬起之前的点
        if isMouseLBDown:
            cv2.line(img, pt1=lastPoint, pt2=(x, y), color=circleColor, thickness=circleRadius)
            lastPoint = (x, y)

# 定义滑动条回调函数，用于更改颜色
def updateCircleColor(x):
    global circleColor
    global colorPreviewImg

    r = cv2.getTrackbarPos('Channel_Red','image')
    g = cv2.getTrackbarPos('Channel_Green','image')
    b = cv2.getTrackbarPos('Channel_Blue','image')

    circleColor = (b, g, r)
    colorPreviewImg[:] = circleColor

# 定义滑动条回调函数，用于更改线条的粗壮
def updateCircleRadius(x):
    global circleRadius
    global radiusPreview

    circleRadius = cv2.getTrackbarPos('Circle_Radius', 'image')
    radiusPreview[:] = (255, 255, 255)
    cv2.circle(radiusPreview, center=(50, 50), radius=int(circleRadius / 2), color=(0, 0, 0), thickness=-1)

# 预览画布用的画布
img = np.ones((512,512,3), np.uint8)
img[:] = (255, 255, 255)

# 预览画笔颜色用的画布
colorPreviewImg = np.ones((100, 100, 3), np.uint8)
colorPreviewImg[:] = (0,  0, 0)

# 预览画笔粗壮用的画布
radiusPreview = np.ones((100, 100, 3), np.uint8)
radiusPreview[:] = (255, 255, 255)

# 预览画布用的窗口
cv2.namedWindow('image')

# 预览画笔颜色用的窗口
cv2.namedWindow('colorPreview')

# 预览画笔粗壮用的窗口
cv2.namedWindow('radiusPreview')

# 画画的鼠标回调，绑定在预览画布窗口上
cv2.setMouseCallback('image',draw_circle)  

# 更改颜色用的滑条回调，绑定在预览画布用的窗口
cv2.createTrackbar('Channel_Red','image',60,255,updateCircleColor)
cv2.createTrackbar('Channel_Green','image',120,255,updateCircleColor)
cv2.createTrackbar('Channel_Blue','image',180,255,updateCircleColor)

# 更改线条粗壮的滑条回调，绑定在预览画布用的窗口
cv2.createTrackbar('Circle_Radius','image',2,20,updateCircleRadius)

while(True):

    # 画布
    cv2.imshow('image',img) 
    # 画笔颜色
    cv2.imshow('colorPreview', colorPreviewImg)
    # 画笔线条粗壮
    cv2.imshow('radiusPreview', radiusPreview)

    if cv2.waitKey(1) == ord('q'):  
        break

cv2.destroyAllWindows()
cv2.imwrite("OpenCV_Paint.png",  img)
