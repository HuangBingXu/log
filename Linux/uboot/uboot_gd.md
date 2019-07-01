# arch_global_data

### 1.定义
在**CPUIDR/include/sam/global_data.h**中定义，
```
/* Architecture-specific global data */
struct arch_global_data {
    #if defined(CONFIG_FSL_ESDHC)
	u32 sdhc_clk;
#endif

#if defined(CONFIG_U_QE)
	u32 qe_clk;
	u32 brg_clk;
	uint mp_alloc_base;
	uint mp_alloc_top;
#endif /* CONFIG_U_QE */
................
#if defined(CONFIG_FSL_LSCH3) && defined(CONFIG_SYS_FSL_HAS_DP_DDR)
	unsigned long mem2_clk;
#endif

#ifdef CONFIG_ARCH_IMX8
	struct udevice *scu_dev;
#endif
};
```





# global_data
### 1. 定义
在文件**u-boot-2018.11\include\asm-generic\global_data.h**中定义：
```
typedef struct global_data {
	bd_t *bd;
	unsigned long flags;
	unsigned int baudrate;
	unsigned long cpu_clk;		/* CPU clock in Hz!		*/
	unsigned long bus_clk;
................
#ifdef CONFIG_LOG
	int log_drop_count;		/* Number of dropped log messages */
	int default_log_level;		/* For devices with no filters */
	struct list_head log_head;	/* List of struct log_device */
	int log_fmt;			/* Mask containing log format info */
#endif
} gd_t;
```


```
#ifdef CONFIG_ARM64
#define DECLARE_GLOBAL_DATA_PTR		register volatile gd_t *gd asm ("x18")
#else
#define DECLARE_GLOBAL_DATA_PTR		register volatile gd_t *gd asm ("r9")
#endif
#endif
```

### 2. 初始化                 
在**u-boot-2018.11\arch\arm\lib\crt0.S**文件中的**_main**有对global_data进行操作：
#### 1.分配空间

>	bl	board_init_f_alloc_reserve

跳转到函数**board_init_f_alloc_reserve**，函数**board_init_f_alloc_reserve**位于：

> u-boot-2018.11\common\init\board_init.c 

```
ulong board_init_f_alloc_reserve(ulong top)
{
	/* Reserve early malloc arena */
#if CONFIG_VAL(SYS_MALLOC_F_LEN)
	top -= CONFIG_VAL(SYS_MALLOC_F_LEN);
#endif

	/* LAST : reserve GD (rounded up to a multiple of 16 bytes) */
	top = rounddown(top-sizeof(struct global_data), 16);

	return top;
}
```
这个函数用于给global_data分配空间，
* 先从顶部向下分配一块CONFIG_SYS_MALLOC_F_LEN大小的空间给early malloc使用,关于CONFIG_SYS_MALLOC_F_LEN可以参考README, 这块内存是用于在relocation前用于给malloc函数提供内存池。
* 继续向下分配sizeof(struct global_data)大小的内存给global_data使用，向下16byte对齐这时候得到的地址就是global_data的地址。
* 将top，也就是global_data的地址返回



#### 2. 初始化

```
	/* set up gd here, outside any C code */
	mov	r9, r0
	bl	board_init_f_init_reserve
```
从注释上就可以知道，这段代码set up gd数据结构，其中函数**board_init_f_init_reserve**在文件**u-boot-2018.11\common\init\board_init.c**中：
```
void board_init_f_init_reserve(ulong base)
{
	struct global_data *gd_ptr;

	/*
	 * clear GD entirely and set it up.
	 * Use gd_ptr, as gd may not be properly set yet.
	 */

	gd_ptr = (struct global_data *)base;
	/* zero the area */
	memset(gd_ptr, '\0', sizeof(*gd));
	/* set GD unless architecture did it already */
#if !defined(CONFIG_ARM)
	arch_setup_gd(gd_ptr);
#endif
	/* next alloc will be higher by one GD plus 16-byte alignment */
	base += roundup(sizeof(struct global_data), 16);

	/*
	 * record early malloc arena start.
	 * Use gd as it is now properly set for all architectures.
	 */

#if CONFIG_VAL(SYS_MALLOC_F_LEN)
	/* go down one 'early malloc arena' */
	gd->malloc_base = base;
	/* next alloc will be higher by one 'early malloc arena' size */
	base += CONFIG_VAL(SYS_MALLOC_F_LEN);
#endif
}
```

1. 对global_data进行清零

2. 因为global_data区域是16Byte对齐的，对齐后，后面的地址就是early malloc的内存池的地址，具体参考上述board_init_f_alloc_reserve，所以这里就获取了early malloc的内存池的地址
3. 将内存池的地址写入到gd->malloc_base中
4. 加上CONFIG_SYS_MALLOC_F_LEN，获取early malloc的内存池的末尾地址，这里并没有什么作用，是为了以后在early malloc的内存池后面多加一个区域时的修改方便。



## 为什么要是用global_data

一、global_data功能
1、global_data存在的意义

在某些情况下，uboot是在某些只读存储器上运行，比如ROM、nor flash等等。
在uboot被重定向到RAM（可读可写）之前，我们都无法写入数据，更无法通过全局变量来传递数据。
而global_data则是为了解决这个问题。
这里顺便一下，后续的uboot的relocation操作，也就是uboot的重定向操作，最主要的目的也是为了解决这个问题，后续会专门说明。
2、 global_data简单介绍

global_data又称之为GD.

简单地说，uboot把global_data放在RAM区，并且使用global_data来存储全局数据。由此来解决上述场景中无法使用全局变量的问题。




# 参考：
[u-boot启动流程分析(2)_板级(board)部分](http://www.wowotech.net/u-boot/boot_flow_2.html)

[Uboot最重要的全局变量gd](https://oska874.github.io/%E6%BA%90%E7%A0%81/uboot%E6%9C%80%E9%87%8D%E8%A6%81%E7%9A%84%E5%85%A8%E5%B1%80%E5%8F%98%E9%87%8Fgd.html)

[[uboot] （番外篇）global_data介绍](https://blog.csdn.net/ooonebook/article/details/53013545)