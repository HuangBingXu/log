import cv2 as cv
import numpy as np


def drawhist(hist):
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9*256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv.line(histImg, (h,256), (h,256-intensity), [255, 0, 0])
    return histImg

img = cv.imread("./../wu.jpg")
hist = cv.calcHist([img],[0],None,[256],[0.0,255.0])
histI = drawhist(hist)
cv.imshow("hist",histI)
cv.waitKey(0)
cv.destroyAllWindows()
