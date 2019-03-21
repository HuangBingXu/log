import cv2
import numpy
import sys

def split_opencv():
    im = cv2.imread("./../test.jpg")
    r, g, b = cv2.split(im)
    cv2.imshow('Red', r)
    cv2.imshow('Green', g)
    cv2.imshow('Blue', b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(r)

def split_numpy():
    im = cv2.imread("./../test.jpg")
    r = numpy.zeros((im.shape[0], im.shape[1]), dtype=im.dtype)
    g = numpy.zeros((im.shape[0], im.shape[1]), dtype=im.dtype)
    b = numpy.zeros((im.shape[0], im.shape[1]), dtype=im.dtype)
    r[:,:] = im[:,:,0]
    g[:,:] = im[:,:,1]
    b[:,:] = im[:,:,2]
    cv2.imshow('Red', r)
    cv2.imshow('Green', g)
    cv2.imshow('Blue', b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(im)
    print(r)

def split_numpy_color():
    im = cv2.imread("./../test.jpg")
    r = numpy.zeros((im.shape[0], im.shape[1],3), dtype=im.dtype)
    g = numpy.zeros((im.shape[0], im.shape[1],3), dtype=im.dtype)
    b = numpy.zeros((im.shape[0], im.shape[1],3), dtype=im.dtype)
    r[:,:,0] = im[:,:,0]
    g[:,:,1] = im[:,:,1]
    b[:,:,2] = im[:,:,2]
    cv2.imshow('Red', r)
    cv2.imshow('Green', g)
    cv2.imshow('Blue', b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(r)
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        split_opencv()
    else:
        if sys.argv[1] == '0':
            split_opencv()
        elif sys.argv[1] == '1':
            split_numpy()
        elif sys.argv[1] =='2':
            split_numpy_color()
        else:
            print("invilid arg")
    te = numpy.zeros((3,3,3))
    print(te)
# 由于 OpenCV-Python 和 NumPy 结合的很紧，所以即可使用 OpenCV自带的 split函数，也可以直接操作 Numpy 数组来分离通道。
# 参考：https://lizonghang.github.io/2016/07/21/OpenCV%E5%83%8F%E7%B4%A0%E4%B8%8E%E9%80%9A%E9%81%93/