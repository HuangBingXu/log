把烧录了固件的SD卡插到Win7，虽然不能通过文件管理器打开查看SD卡，还是可以用WinHex打开，打开后如下：

![](sd_winhex/first.png)





把有固件的SD卡用读卡器接到Linux PC，会有4个磁盘，如下：

![](sd/mout_in_linux.png)

正好与win7中用winHex打开，看到的4个Ext4格式的分区对应，

4个分区中的文件为：

* ##### bootfs

  ![](sd/bootfs1.png)

* ###### rootfs

  ![](sd/rootfs.png)

* ##### userfs

  ![](sd/userfs.png)

* vendorfs

  ![](sd/vendorfs.png)