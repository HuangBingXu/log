最近RT-Thread重新整理了STM32系列BSP，推出了新的BSP框架，正好手上有一块 **[B-L475E-IOT01A](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html)**，可以用来体验下新的BSP。

B-L475E-IOT01A是ST基于STM32L475VG推出的一个面向IOT的DEMO板，具体介绍请查看[官网](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html)。

### 准备环境：
1. RT-Thread Env工具，Env官方介绍如下：
> RT-Thread Env工具包括配置器和包管理器，用来对内核和组件的功能进行配置，对组件进行自由裁剪，对线上软件包进行管理，使得系统以搭积木的方式进行构建，简单方便。

下载地址为：[https://www.rt-thread.org/page/download.html](https://www.rt-thread.org/page/download.html)

2. 下载RT-Thread                  
    直接从RT-Thread github clone下来：
> git clone https://github.com/RT-Thread/rt-thread.git

    
### 移植BSP到B-L475E-IOT01A
这里移植步骤是根据[STM32 系列 BSP 制作教程](https://github.com/RT-Thread/rt-thread/blob/master/bsp/stm32/docs/STM32%E7%B3%BB%E5%88%97BSP%E5%88%B6%E4%BD%9C%E6%95%99%E7%A8%8B.md)来操作的。

##### 1. 首先把**rt-thread\bsp\stm32\libraries\templates** 目录下的 **stm32l4xx**文件夹复制到**rt-thread\bsp\stm32**，并重命名为**stm32l475-iot-disco**，

##### 2. 用CubeMX重新生成项目
打开**stm32l475-iot-disco\board\CubeMX_Config**下的**CubeMX_Config.ioc**，如下图：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/08F51682C6DA4CC49C13DA053B9E2DF7/10347)


由于默认的并不是该板子上的STM32L475VG，需要修改芯片的型号，由于CubeMX不支持重新选择芯片型号，需要新建工程，重新选择芯片型号（点击上图中STM32L475VETX（home旁边）即可重新创建工程，），然后按照教程修改时钟、打开串口、设置下载方式。设置完成后保存并生成项目，



![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/63C8B79290BE497A84CF4DBE79519488/10376)

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/AF7FCCC9641D4206876BC0F4D06C8123/10375)

用CubeMX重新生成代码后，拷贝初始化函数，即把**board/CubeMX_Config/Src/main.c**里面的时钟初始化函数**SystemClock_Config**替换**board/board.c**里面的时钟初始化函数**SystemClock_Config**。



然后按照教程修改Kconfig文件（board/Kconfig），修改脚本文件，修改工程文件。

3. 根据板子外设修改例程，并编译测试

**applications**下面的**mian.c**中有个控制等闪烁的例子，该板子LED部分原理如下：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/5935B7CCEA3E424A97D92AB034D7045E/10422)

这里选择使用LED2，通过查看原理图，LED2是连接到了PB14，把控制led的IO改为PB14，并加上一条语句，输出**HEllo This is the BSP for B-L475E-IOT01A(STM32L475VG)**代码修改为：


```
#define LED0_PIN    GET_PIN(B, 14)

int main(void)
{
    int count = 1;
    /* set LED0 pin mode to output */
    rt_pin_mode(LED0_PIN, PIN_MODE_OUTPUT);
    rt_kprintf("\r\nHello This is the BSP for B-L475E-IOT01A(STM32L475VG)\r\n");
    while (count++)
    {
        rt_pin_write(LED0_PIN, PIN_HIGH);
        rt_thread_mdelay(500);
        rt_pin_write(LED0_PIN, PIN_LOW);
        rt_thread_mdelay(500);
    }

    return RT_EOK;
}
```
然后用RT-Thread Env工具编译工程，把固件下载到板子上，运行如下：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/4D0570D4D3224A3E8609F92E15BEE277/10444)



#### 填的坑
1. 该板子有带USB CDC（usb转串口）设备的ST-LINK，并接到了STM32L475VG的Uart1,如下图，因此，可以不用其他的串口设备，可以直接使用这个ST-LINK上的CDC设备实现STM32L475通过串口跟PC连接，来查看调试信息，

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/4CF50F938D6B4E099915683E61435082/10480)

一开始不管我怎么调，都没有调试信息出来，确认了原理图是UART1，又确认了代码是UART1，最后仔细查看了原理图，发现MCU部分UART1是使用了PB6跟PB7，如下图

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/A84D189E781D49479A324A7F8C8FB26F/10485)

所以，CubeMX中配置UART1的时候需要把UART的RX、TX重映射到PB6、PB7，
