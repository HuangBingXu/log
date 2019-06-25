## 1、U_BOOT_DRIVER
U_BOOT_DRIVER是一个宏，在**u-boot-2018.11\include\dm\device.h**中定义，如下：
```
/* Declare a new U-Boot driver */
#define U_BOOT_DRIVER(__name)						\
	ll_entry_declare(struct driver, __name, driver)
```

通过查看源码，发现**ll_entry_declare**也是一个宏，在文件**u-boot-2018.11\include\linker_lists.h**，如下：
```
#define ll_entry_declare(_type, _name, _list)				\
	_type _u_boot_list_2_##_list##_2_##_name __aligned(4)		\
			__attribute__((unused,				\
			section(".u_boot_list_2_"#_list"_2_"#_name)))
```

则，U_BOOT_DRIVER最终展开为：
```
#define U_BOOT_DRIVER(__name)	        \
struct driver _u_boot_list_2_driver_2_##_name
__aligned(4)
__attribute__((unused,section(".u_boot_list_2_driver_2_"#_name)))
```

**__attribute__((unused))**的意思是告诉编译器表示该函数或变量可能不使用，这个属性可以避免编译器产生警告信息 

大概意思为：
定义一个名为**_u_boot_list_2_driver_2_##_name**的driver结构体，4字对齐

**driver**结构体为：
```
struct driver {
	char *name;
	enum uclass_id id;
	const struct udevice_id *of_match;
	int (*bind)(struct udevice *dev);
	int (*probe)(struct udevice *dev);
	int (*remove)(struct udevice *dev);
	int (*unbind)(struct udevice *dev);
	int (*ofdata_to_platdata)(struct udevice *dev);
	int (*child_post_bind)(struct udevice *dev);
	int (*child_pre_probe)(struct udevice *dev);
	int (*child_post_remove)(struct udevice *dev);
	int priv_auto_alloc_size;
	int platdata_auto_alloc_size;
	int per_child_auto_alloc_size;
	int per_child_platdata_auto_alloc_size;
	const void *ops;	/* driver-specific operations */
	uint32_t flags;
};
```
在**u-boot-2018.11\include\dm\device.h**中定义。




## 术语

Uclass - a group of devices which operate in the same way. A uclass provides
	a way of accessing individual devices within the group, but always
	using the same interface. For example a GPIO uclass provides
	operations for get/set value. An I2C uclass may have 10 I2C ports,
	4 with one driver, and 6 with another.

Driver - some code which talks to a peripheral and presents a higher-level
	interface to it.

Device - an instance of a driver, tied to a particular port or peripheral.