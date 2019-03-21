import cv2 as cv

img = cv.imread("D:\test.jpg")
if img is not None:
    print(img)
    cv.namedWindow("Image")
    cv.imshow("Image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("img is None")