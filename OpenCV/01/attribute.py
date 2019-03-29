import cv2 as cv
import numpy

img = cv.imread("./../test.jpg")
gray = cv.imread("./../test.jpg",0)
print("The color img:")
print(img.shape)
print(img.size)
print(img.dtype)
print("\r\n")
print("The gray img:")
print(gray.shape)
print(gray.size)
print(img.dtype)

# 获取图像的属性：
# * 尺寸（行、列、通道）
# * 像素数目
# * 数据类型