启动流程：
1. SPL
```
    u-boot-stm32mp-2018.11-r0\u-boot-2018.11\arch\arm\cpu\armv7\start.S --> reset  --> cpu_init_crit
        |
        |
        V
    u-boot-2018.11\arch\arm\cpu\armv7\lowlevel_init.S -->  lowlevel_init
        |
        |
        V
    u-boot-2018.11\arch\arm\lib\crt0.S  -->  _main

```

```
	/*
	 * disable interrupts (FIQ and IRQ), also set the cpu to SVC32 mode,
	 * except if in HYP mode already
	 */
	mrs	r0, cpsr
	and	r1, r0, #0x1f		@ mask mode bits
	teq	r1, #0x1a		@ test for HYP mode
	bicne	r0, r0, #0x1f		@ clear all mode bits
	orrne	r0, r0, #0x13		@ set SVC mode
	orr	r0, r0, #0xc0		@ disable FIQ and IRQ
	msr	cpsr,r0

/*
 * Setup vector:
 * (OMAP4 spl TEXT_BASE is not 32 byte aligned.
 * Continue to use ROM code vector only in OMAP4 spl)
 */
#if !(defined(CONFIG_OMAP44XX) && defined(CONFIG_SPL_BUILD))
	/* Set V=0 in CP15 SCTLR register - for VBAR to point to vector */
	mrc	p15, 0, r0, c1, c0, 0	@ Read CP15 SCTLR Register
	bic	r0, #CR_V		@ V = 0
	mcr	p15, 0, r0, c1, c0, 0	@ Write CP15 SCTLR Register

#ifdef CONFIG_HAS_VBAR
	/* Set vector address in CP15 VBAR register */
	ldr	r0, =_start
	mcr	p15, 0, r0, c12, c0, 0	@Set VBAR
#endif
#endif

	/* the mask ROM code should have PLL and others stable */
#ifndef CONFIG_SKIP_LOWLEVEL_INIT
#ifdef CONFIG_CPU_V7A
	bl	cpu_init_cp15
#endif
#ifndef CONFIG_SKIP_LOWLEVEL_INIT_ONLY
	bl	cpu_init_crit
#endif
#endif

	bl	_main
```
上面代码做了：

1. 通过设置CPSR寄存器里设置CPU为SVC模式，禁止中断

2. 调用cpu_init_cp15，初始化协处理器CP15,从而禁用MMU和TLB。**cpu_init_cp15**函数在u-boot-stm32mp-2018.11-r0\u-boot-2018.11\arch\arm\cpu\armv7\start.S中
   
3. cpu_init_crit，进行一些关键的初始化动作，也就是平台级和板级的初始化，其代码核心就是lowlevel_init，**cpu_init_crit**函数在u-boot-stm32mp-2018.11-r0\u-boot-2018.11\arch\arm\cpu\armv7\start.S，
**lowlevel_init**在               **u-boot-stm32mp-2018.11-r0\u-boot-2018.11\arch\arm\cpu\armv7\lowlevel_init.S**中，

4. 然后调用**_main**,**_main**在**u-boot-2018.11\arch\arm\lib\crt0.S**
   * board_init_f
进入 board_init_f() 后会分步骤的初始化外设、将代码拷贝到 DDR 内存。
```
void board_init_f(ulong boot_flags)
{
...
    if (initcall_run_list(init_sequence_f))
        hang();       
...
}
```
initcall_run_list() 用来执行结构体数组 init_sequence_f 定义的一系列配置初始化函数，而 init_sequence_f 包含的初始化函数如下：
```
static const init_fnc_t init_sequence_f[] = {
	setup_mon_len,
#ifdef CONFIG_OF_CONTROL
	fdtdec_setup,
#endif
#ifdef CONFIG_TRACE
	trace_early_init,
#endif
	initf_malloc,
	log_init,
	initf_bootstage,	/* uses its own timer, so does not need DM */
	initf_console_record,
#if defined(CONFIG_HAVE_FSP)
	arch_fsp_init,
#endif
	arch_cpu_init,		/* basic arch cpu dependent setup */
	mach_cpu_init,		/* SoC/machine dependent CPU setup */
	initf_dm,
	arch_cpu_init_dm,
#if defined(CONFIG_BOARD_EARLY_INIT_F)
	board_early_init_f,
#endif
#if defined(CONFIG_PPC) || defined(CONFIG_SYS_FSL_CLK) || defined(CONFIG_M68K)
	/* get CPU and bus clocks according to the environment variable */
	get_clocks,		/* get CPU and bus clocks (etc.) */
#endif
#if !defined(CONFIG_M68K)
	timer_init,		/* initialize timer */
#endif
#if defined(CONFIG_BOARD_POSTCLK_INIT)
	board_postclk_init,
#endif
	env_init,		/* initialize environment */
	init_baud_rate,		/* initialze baudrate settings */
	serial_init,		/* serial communications setup */
	console_init_f,		/* stage 1 init of console */
	display_options,	/* say that we are here */
	display_text_info,	/* show debugging info if required */
#if defined(CONFIG_PPC) || defined(CONFIG_SH) || defined(CONFIG_X86)
	checkcpu,
#endif
#if defined(CONFIG_SYSRESET)
	print_resetinfo,
#endif
#if defined(CONFIG_DISPLAY_CPUINFO)
	print_cpuinfo,		/* display cpu info (and speed) */
#endif
#if defined(CONFIG_DTB_RESELECT)
	embedded_dtb_select,
#endif
#if defined(CONFIG_DISPLAY_BOARDINFO)
	show_board_info,
#endif
	INIT_FUNC_WATCHDOG_INIT
#if defined(CONFIG_MISC_INIT_F)
	misc_init_f,
#endif
	INIT_FUNC_WATCHDOG_RESET
#if defined(CONFIG_SYS_I2C)
	init_func_i2c,
#endif
#if defined(CONFIG_VID) && !defined(CONFIG_SPL)
	init_func_vid,
#endif
#if defined(CONFIG_HARD_SPI)
	init_func_spi,
#endif
	announce_dram_init,
	dram_init,		/* configure available RAM banks */
#ifdef CONFIG_POST
	post_init_f,
#endif
	INIT_FUNC_WATCHDOG_RESET
#if defined(CONFIG_SYS_DRAM_TEST)
	testdram,
#endif /* CONFIG_SYS_DRAM_TEST */
	INIT_FUNC_WATCHDOG_RESET

#ifdef CONFIG_POST
	init_post,
#endif
	INIT_FUNC_WATCHDOG_RESET
	/*
	 * Now that we have DRAM mapped and working, we can
	 * relocate the code and continue running from DRAM.
	 *
	 * Reserve memory at end of RAM for (top down in that order):
	 *  - area that won't get touched by U-Boot and Linux (optional)
	 *  - kernel log buffer
	 *  - protected RAM
	 *  - LCD framebuffer
	 *  - monitor code
	 *  - board info struct
	 */
	setup_dest_addr,
#ifdef CONFIG_PRAM
	reserve_pram,
#endif
	reserve_round_4k,
#ifdef CONFIG_ARM
	reserve_mmu,
#endif
	reserve_video,
	reserve_trace,
	reserve_uboot,
	reserve_malloc,
	reserve_board,
	setup_machine,
	reserve_global_data,
	reserve_fdt,
	reserve_bootstage,
	reserve_arch,
	reserve_stacks,
	dram_init_banksize,
	show_dram_config,
#if defined(CONFIG_M68K) || defined(CONFIG_MIPS) || defined(CONFIG_PPC) || \
	defined(CONFIG_SH)
	setup_board_part1,
#endif
#if defined(CONFIG_PPC) || defined(CONFIG_M68K)
	INIT_FUNC_WATCHDOG_RESET
	setup_board_part2,
#endif
	display_new_sp,
#ifdef CONFIG_OF_BOARD_FIXUP
	fix_fdt,
#endif
	INIT_FUNC_WATCHDOG_RESET
	reloc_fdt,
	reloc_bootstage,
	setup_reloc,
#if defined(CONFIG_X86) || defined(CONFIG_ARC)
	copy_uboot_to_ram,
	do_elf_reloc_fixups,
	clear_bss,
#endif
#if defined(CONFIG_XTENSA)
	clear_bss,
#endif
#if !defined(CONFIG_ARM) && !defined(CONFIG_SANDBOX) && \
		!CONFIG_IS_ENABLED(X86_64)
	jump_to_copy,
#endif
	NULL,
};
```
init_sequence_f 因为要支持多种处理器、多种外设、多种配置，所以会很长，但是针对特定的开发板只需要其中的某几个函数即可，而且针对 armv7 需要重点关注的函数有以下几个：
```
serial_init,        /* serial communications setup */
console_init_f,     /* stage 1 init of console */
INIT_FUNC_WATCHDOG_INIT,
INIT_FUNC_WATCHDOG_RESET,
dram_init,      /* configure available RAM banks */
setup_dest_addr,
setup_reloc,
```
* 其中 serial_init ， console_init_f ， dram_init 是用来配置硬件外设和相关数据结构 ，
    如 serial_init() 会将外设驱动和 gd 关联起来（gd->cur_serial_dev = dev;），以后要使用串口就不需要直接调用具体的外设驱动了。

* setup_dest_addr 、 setup_reloc 、 一起设置 uboot 代码在内存中的位置，为接下来将代码拷贝到内存做准备。

执行完 board_init_f 配置好相关数据结构、变量后， uboot 会调用 relocate_code 进行重定位代码，会把代码拷贝到 ddr 内存，

* 然后调用 board_init_r 真正的初始化、启动硬件。board_init_r 和 board_init_f 结构类似，都是执行一连串的初始化函数：
  
参考：
[U-BOOT移植过程详解: SPL](http://www.voidcn.com/article/p-fjqavebr-p.html)
[[uboot] （第三章）uboot流程——uboot-spl代码流程](https://blog.csdn.net/ooonebook/article/details/52957395)
[Uboot启动流程](https://oska874.github.io/%E6%BA%90%E7%A0%81/uboot%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html)