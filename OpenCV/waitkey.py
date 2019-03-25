import cv2 as cv

def wait_key():
    cv.waitKey(0)
    cv.destroyAllWindows()