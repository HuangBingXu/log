# https://docs.opencv.org/master/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2 as cv


def harris_detection():
    img = cv.imread("./../wu.jpg")
    if img is None:
        print("read img faile")
        exit()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv.imshow('dst',img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


def sift_detection():
    img = cv.imread('./../wu.jpg')
    gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    sift = cv.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    img=cv.drawKeypoints(gray,kp,img)
    cv.show('sift_keypoints',img)
    
# 用默认的方法安装python，会有如下错误：
# module 'cv2.cv2' has no attribute 'xfeatures2d'
# 按照网上的方法，如下：pip install opencv-contrib-python
# 还会有如下问题：
# cv2.error: OpenCV(4.0.0) C:\projects\opencv-python\opencv_contrib\modules\xfeatures2d\src\sift.cpp:1207: 
# error: (-213:The function/feature is not implemented) This algorithm is patented and is excluded in this configuration; 
# Set OPENCV_ENABLE_NONFREE CMake option and rebuild the library in function 'cv::xfeatures2d::SIFT::create'

if __name__ == "__main__":
    sift_detection();