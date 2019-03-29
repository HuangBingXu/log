import cv2 as cv
import numpy as np

img = cv.imread("code.jpg",0)
cv.imshow("src",img)
out = np.full(img.shape,255,img.dtype)
cv.normalize(img,img,0,255,cv.NORM_MINMAX)
print(img)
cv.imshow("nor",img)
cv.waitKey(0)
cv.destroyAllWindows()
