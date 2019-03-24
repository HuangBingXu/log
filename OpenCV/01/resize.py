import cv2 as cv

img = cv.imread("./../2.png")
if img is None:
    print("Open img faile,exit app")
    exit()
res = cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
# or
# res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
cv.imshow("res",res)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()

#  dst	=	cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	)
