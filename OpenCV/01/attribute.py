import cv2 as cv
import numpy

img = cv.imread("./../test.jpg")
print(img.shape)
print(img.size)
print(img.dtype)

# 获取图像的属性：
# * 尺寸（行、列、通道）
# * 像素数目
# * 数据类型