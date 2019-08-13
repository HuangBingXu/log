###### u-boot-2018.11\MAINTAINERS

列出了uboot中的组建由什么人编写维护（给出了名字，邮件），该组件的git地址，相关目录及文件，该组件的状态（Supported、Maintained、Odd Fixes、Orphan、Obsolete等）



#### CHANGELOG

记录移植信息（？）

2010.8开始，uboot源码中不再有CHANGELOG文件，但可以通过如下命令获得CHANGELOG文件(从git log获取)：

> make CHANGELOG





2008.10开始使用年月来给uboot设置版本号

u-boot自`v2014.10`版本开始引入KBuild系统