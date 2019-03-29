import cv2 as cv
from pyzbar.pyzbar import decode

img = cv.imread("qrcode.jpg")
result = decode(img)
print(result)