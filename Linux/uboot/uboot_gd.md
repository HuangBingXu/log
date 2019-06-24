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
在**u-boot-2018.11\arch\arm\lib\crt0.S**文件中有这么一段代码：
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




# 参考：
[u-boot启动流程分析(2)_板级(board)部分](http://www.wowotech.net/u-boot/boot_flow_2.html)

[Uboot最重要的全局变量gd](https://oska874.github.io/%E6%BA%90%E7%A0%81/uboot%E6%9C%80%E9%87%8D%E8%A6%81%E7%9A%84%E5%85%A8%E5%B1%80%E5%8F%98%E9%87%8Fgd.html)