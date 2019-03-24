import cv2 as cv
import numpy

# openCV的加法（cv.add）是一种饱和操作
# numpy的加法是一种模操作

# 图像混合
# 这也是加法，不同的是两幅图像的权重不同，这会给人一种混合或者透明的感觉。图像混合的计算公式如下：
# g(x) = (1−α)f0 (x)+αf1 (x)
# 通过修改α的值（0-->1）,可以实现很酷的混合。
def img_add_use_weight():
    img1 = cv.imread("./../2.png")
    img2 = cv.imread("./../test.jpg")
    dst = cv.addWeighted(img1,0.7,img2,0.3,0)
    cv.imshow("dst",dst)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__=="__main__":
    img_add_use_weight()