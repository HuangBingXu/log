import cv2 as cv
import numpy
import sys

def merge_raw():
    im = cv.imread('./../test.jpg')
    r,g,b = cv.split(im)
    merged = numpy.dstack([b,r,g])
    cv.imshow('merge', merged)
    cv.waitKey(0)
    cv.destroyAllWindows()

def merge_with_other():
    im = cv.imread('./../test.jpg')
    im_2 = cv.imread('./../2.png')
    r,g,b = cv.split(im)
    r_2,g_2,b_2 = cv.split(im_2)
    merged = numpy.dstack([r,g_2,b_2])
    cv.imshow('merge', merged)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("argv 0")
        merge_raw()
    else:
        if sys.argv[1] =='1':
            print("argv 1")
            merge_raw()
        elif sys.argv[1] == '2':
            print("argv 2")
            merge_with_other()
        else:
            print("argv error")
# 参考：https://lizonghang.github.io/2016/07/21/OpenCV%E5%83%8F%E7%B4%A0%E4%B8%8E%E9%80%9A%E9%81%93/
# 可是看不出这个有什么效果
# 这里讲的是独立的通道的图片合成一个RGB，由于合成的通道是原图分离出来的，所以没变化
# 如果用两张图片中的某些通道合并成一张图片，既可以看出差异了