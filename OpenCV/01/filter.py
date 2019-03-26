import cv2 as cv


def lowpass_filter():
    img = cv.imread("./../wu.jpg")
    blured = cv.blur(img,(5,5))

    cv.imshow("src",img)
    cv.imshow("blured",blured)
    cv.waitKey(0)
    cv.destroyAllWindows()
# 初级低通滤波
# 低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值，这样就可以平滑并替代那些强度变化明显的区域。
# 在 OpenCV 中可以通过 cv2.blur() 来实现
# 这种滤波器又称为 boxfilter，所以也可使用 cv2.boxFilter() 完成相同的工作。如下：
# dst = cv2.boxFilter(im, -1, (5,5))
# 该函数与 cv2.blur() 效果完全相同，第二个参数 -1 表示输出图像使用的深度与输入图像相同

def gauss_filter():
    img = cv.imread("./../wu.jpg")
    blured = cv.GaussianBlur(img,(5,5),1.5)

    cv.imshow("src",img)
    cv.imshow("blured",blured)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 高斯模糊
# 在某些情况下需要对一个像素的周围像素给予更多的重视。因此可用分配权重来重新计算这些周围点的值，
# 可以通过高斯函数的权重方案来解决

# 高斯滤波跟低通滤波的区别
# 低通滤波与高斯滤波不同之处在于：低通滤波中，滤波器中每个像素的权重是相同的，即滤波器是线性的。
# 而高斯滤波器中像素的权重与其距中心像素的距离成比例。

def median_filter():
    img = cv.imread("./../wu.jpg")
    blured = cv.medianBlur(img,5)

    cv.imshow("src",img)
    cv.imshow("blured",blured)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 中值滤波
# 消除噪点
# 中值滤波器对于消除椒盐现象很有用

if __name__ == "__main__":
    median_filter()