#### 整体构架

* udevice

  指设备对象

* driver

  udevice的驱动，可以理解为kernel中的device_driver。和底层硬件设备通信，并且为设备提供面向上层的接口。

* uclass

  uclass，使用相同方式的操作集的device的组，uclass为那些使用相同接口的设备提供了统一的接口

* uclass_driver

  对应uclass的驱动程序。主要提供uclass操作时，如绑定udevice时的一些操作



``````mermaid

graph TD

	A[Driver modle] -->B(Uclass)

    A[Driver modle] --> C(Driver)

    A[Driver modle] --> D(Device)
``````





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



```
struct uclass {
	void *priv;
	struct uclass_driver *uc_drv;
	struct list_head dev_head;
	struct list_head sibling_node;
};
```

```
struct udevice {
	const struct driver *driver;
	const char *name;
	void *platdata;
	void *parent_platdata;
	void *uclass_platdata;
	ofnode node;
	ulong driver_data;
	struct udevice *parent;
	void *priv;
	struct uclass *uclass;
	void *uclass_priv;
	void *parent_priv;
	struct list_head uclass_node;
	struct list_head child_head;
	struct list_head sibling_node;
	uint32_t flags;
	int req_seq;
	int seq;
#ifdef CONFIG_DEVRES
	struct list_head devres_head;
#endif
};
```





## derive modle demo

#### cmd demo

> u-boot\cmd\demo.c

该文件实现了一些用来测试driver model demo 的驱动的命令

#### driver demo:

> u-boot\drivers\demo\\*