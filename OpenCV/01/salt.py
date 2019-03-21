import cv2 as cv
import numpy

def salt(img,n):
    for k in range(n):
        i = int(numpy.random.random() * img.shape[1])
        j = int(numpy.random.random() * img.shape[0])
        if img.ndim ==2:
            img[j,i] == 255
        elif img.ndim ==3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img

if __name__ == '__main__':
    img = cv.imread("./../test.jpg")
    saltImg = salt(img,1000)
    cv.imshow("SaltImage",saltImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

# python中判断图片通道数使用img.ndim
# img.ndin =2: 表示灰度
# img.ndin =3：表示彩色（3通道）

# python中使用数组方式操作像素,如把（x，y)像素都设为255：
# * 灰度            
# img[x,y] = 255
# * 彩色
# img[x,y,0] = 255                
# img[x,y,1] = 255               
# img[x,y,2] = 255   