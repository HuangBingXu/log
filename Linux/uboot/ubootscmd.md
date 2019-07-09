1. make help
查看uboot命令及其使用方法，也可以查看README文件

2. make menuconfig
配置参数

3. make sandbox_defconfig
如果没有合适的运行环境（开发板）运行 uboot 镜像，可以编译 sandbox 版的 uboot ， 这样就可以想运行程序一样运行 uboot 镜像

* 编译
```
make sandbox_defconfig
make
```
* 运行
```
u-boot-2016.07-rc2 ./u-boot -d u-boot.dtb
```

