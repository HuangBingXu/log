cmd中获取设备

获取设备信息

设备在设备树中的信息

gd->fdt_blob已经设置成了dtb的地址了





```
	printf("Test device:%s\n",argv[1]);
	int get_device_status = uclass_get_device_by_name(UCLASS_GPIO,argv[1],&dev);
	printf("The status is:%d\n",get_device_status);
	printf("uClass's name:%s\n",dev_get_uclass_name(dev));
	printf("Device's name:%s\n",dev->name);
	printf("Device's driver's name:%s\n",dev->driver->name);
	// gpio-bank-name
	printf("%s,%s\n",fdt_getprop(gd->fdt_blob, dev_of_offset(dev),"gpio-bank-name", &len),dev_read_string(dev, "gpio-bank-name"));
	printf("%d,%d\n",len,dev_read_u32_default(dev, "sandbox,gpio-count",0));
```

运行结果：

![](test.png)

得不到想要的结果，获取不了**gpio-bank-name**的值

