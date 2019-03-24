import cv2 as cv
import numpy as np
img = cv.imread("./../wu.jpg")
cv.imshow("src",img)

kernel = np.ones((5,5),np.uint8)
erode = cv.erode(img,kernel,iterations=1)
dilation = cv.dilate(img,kernel,iterations=1)
opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow("close",closing)
cv.imshow("open",opening)
cv.imshow("erode",erode)
cv.imshow("dilation",dilation)
cv.imshow("gradient",gradient)
cv.imshow("tophat",tophat)
cv.imshow("blackhat",blackhat)

cv.waitKey(0)
cv.destroyAllWindows()
