###  环境
* win10 64bit 家庭中文版
* python 
> Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32



### 安装OpenCV(2019\03\21)
[参考](https://www.cnblogs.com/lclblack/p/6377710.html)
```
pip install --upgrade setuptools
pip install numpy Matplotlib
pip install opencv-python
```

安装 opencv的版本是：
> opencv-python-4.0.0.21


### 测试
```
import cv2 as cv

img = cv.imread("D:\\test.jpg")
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()
```

**注意，文件路劲斜杠需要用两个\\，一开始只用一个，不能成功打开文件**

如果打开文件失败的话会有如下错误：
```
  File ".\01.py", line 6, in <module>
    cv.imshow("Image",img)
cv2.error: OpenCV(4.0.0) C:\projects\opencv-python\opencv\modules\highgui\src\window.cpp:350: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
```
把代码改为如下,添加img为空判断，可以避免这个问题：
```
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
```


### 读取图片并显示
上述代码的功能就是读取图片并显示出来，使用到的API有：
#### imshow 读取图片                 
第一个参数是打开文件路径                     
第二个参数是读取图片的方式                
* cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.                                       
* cv.IMREAD_GRAYSCALE : Loads image in grayscale mode                  
* cv.IMREAD_UNCHANGED : Loads image as such including alpha channel   

以上3个参数分别可以用1、0、-1表示                         

**Even if the image path is wrong, it won't throw any error, but print img will give you None**

#### imshow() 显示图片
第一个参数是显示窗口的名字
第二个参数是要显示的图片