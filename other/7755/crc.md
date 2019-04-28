## 1、先计算出需要写入的数组的CRC，使用的CRC算法为：
> G(x)=x16+x12+x5+1
#### 获取方法：
1. 使用Control Software获取CRC校验，如下图：
   ![](G:\mics\log\log\other\7755\img\control_software_crc.png)

2. 使用其他工具获取CRC校验，如下图，使用网上校验工具：

![](G:\mics\log\log\other\7755\img\online_tool_crc.png)

## 2、编程写入IC

1. 先写入数组，然后写入CRC，读取CRC校验结果，
2. 写入数组，然后读取CRC，比较读取来的与计算出来的CRC，