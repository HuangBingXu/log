### Mat
参考：[OpenCV 编程简介（矩阵/图像/视频的基本读写操作）](http://wiki.opencv.org.cn/index.php/OpenCV_%E7%BC%96%E7%A8%8B%E7%AE%80%E4%BB%8B%EF%BC%88%E7%9F%A9%E9%98%B5/%E5%9B%BE%E5%83%8F/%E8%A7%86%E9%A2%91%E7%9A%84%E5%9F%BA%E6%9C%AC%E8%AF%BB%E5%86%99%E6%93%8D%E4%BD%9C%EF%BC%89)
```
CvMat                      // 2D 矩阵
  |-- int   type;          // 元素类型 (uchar,short,int,float,double) 与标志
  |-- int   step;          // 整行长度字节数
  |-- int   rows, cols;    // 行、列数
  |-- int   height, width; // 矩阵高度、宽度，与rows、cols对应
  |-- union data;
      |-- uchar*  ptr;     // data pointer for an unsigned char matrix
      |-- short*  s;       // data pointer for a short matrix
      |-- int*    i;       // data pointer for an integer matrix
      |-- float*  fl;      // data pointer for a float matrix
      |-- double* db;      // data pointer for a double matrix
```

          
