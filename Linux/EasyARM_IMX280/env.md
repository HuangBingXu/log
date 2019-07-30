编译工具：“gcc-4.4.4-glibc-2.11.1-multilib-1.0_EasyARM-iMX283.tar.bz2”

* 可以在光盘目录**“\3、Linux\2、工具软件\Linux工具软件”**下找到

*  由于编译工具是32bit，如果是在64bit系统中使用需要安装32bit兼容库（ubuntu 1604中测试）

> sudo apt-get install lib32ncurses5 lib32z1

* 可以在**/etc/profile **添加该编译工具路径，

