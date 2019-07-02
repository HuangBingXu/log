#### 1. 获取u-boot源码

> git clone  https://gitlab.denx.de/u-boot/u-boot.git

#### 2、编译

进入u-boot目录，编译：

```
   make sandbox_defconfig
   make
```

![](G:\mics\log\log\Linux\uboot\img\build_sandbox.png)

#### 3、运行

> ./u-boot -d u-boot.dtb

![](G:\mics\log\log\Linux\uboot\img\run_sandbox.png)