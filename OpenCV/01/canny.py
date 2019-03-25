import cv2 as cv
import numpy as np

img = cv.imread("./../wu.jpg")
img = cv.GaussianBlur(img,(3,3),0)
canny = cv.Canny(img,30,100)
cv.imshow("Canny",canny)
cv.waitKey(0)
cv.destroyAllWindows()