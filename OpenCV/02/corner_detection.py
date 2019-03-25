import cv2 as cv 

#open img in gray way
img = cv.imread("./../wu.jpg",0)

cross = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
diamond = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
diamond[0,0], diamond[0,1], diamond[1,0], diamond[4,4], diamond[4,3], diamond[3,4], diamond[4,0], diamond[4,1], diamond[3,0], diamond[0,3], diamond[0,4], diamond[1,4] = 0,0,0,0,0,0,0,0,0,0,0,0
square = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
x = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

detect1 = cv.dilate(img, cross)
detect1 = cv.erode(detect1, diamond)
detect2 = cv.dilate(img, x)
detect2 = cv.erode(detect2, square)
horn = cv.absdiff(detect2, detect1)
cv.imshow("Horn",horn)
retval, horn = cv.threshold(horn, 40, 255, cv.THRESH_BINARY)

for j in range(horn.size):
    y = int(j / horn.shape[0])
    x = j % horn.shape[0]
    # print(x,y)
    if horn[x,y] == 255:
        cv.circle(img, (y,x), 5, (255,0,0))

cv.imshow("Horn Detect",img)
cv.waitKey(0)
cv.destroyAllWindows()