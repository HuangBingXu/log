import cv2 as cv
import numpy as np

img = cv.imread("./../wu.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# or gray  = cv.imread("./../wu.jpg")

kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))

dilated = cv.dilate(gray,kernel)
eroded = cv.erode(gray,kernel)

edges = cv.absdiff(dilated, eroded)
cv.imshow("edge",edges)
retval, edges = cv.threshold(edges, 50, 100, cv.THRESH_BINARY)
edges = cv.bitwise_not(edges)

cv.imshow("src",img)
cv.imshow("edges",edges)

cv.waitKey(0)
cv.destroyAllWindows()


# 检测边缘
# 形态学检测边缘的原理为：在膨胀时图像中的物体会想向周围扩张；腐蚀时图像中的物体会收缩。
# 比较这两幅图像，由于其变化的区域只发生在边缘，所以将两幅图像相减，得到的就是图像中物体的边缘。