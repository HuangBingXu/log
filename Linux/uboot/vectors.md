该文件位于：**u-boot-2018.11\arch\arm\lib\vectors.S**

```
/* SPDX-License-Identifier: GPL-2.0+ */
/*
 *  vectors - Generic ARM exception table code
 *
 *  Copyright (c) 1998	Dan Malek <dmalek@jlc.net>
 *  Copyright (c) 1999	Magnus Damm <kieraypc01.p.y.kie.era.ericsson.se>
 *  Copyright (c) 2000	Wolfgang Denk <wd@denx.de>
 *  Copyright (c) 2001	Alex Züpke <azu@sysgo.de>
 *  Copyright (c) 2001	Marius Gröger <mag@sysgo.de>
 *  Copyright (c) 2002	Alex Züpke <azu@sysgo.de>
 *  Copyright (c) 2002	Gary Jennejohn <garyj@denx.de>
 *  Copyright (c) 2002	Kyle Harris <kharris@nexus-tech.net>
 */

#include <config.h>
```
ARM通用异常向量表


```
/*
 * A macro to allow insertion of an ARM exception vector either
 * for the non-boot0 case or by a boot0-header.
 */
        .macro ARM_VECTORS
#ifdef CONFIG_ARCH_K3
	ldr     pc, _reset
#else
	b	reset
#endif
	ldr	pc, _undefined_instruction
	ldr	pc, _software_interrupt
	ldr	pc, _prefetch_abort
	ldr	pc, _data_abort
	ldr	pc, _not_used
	ldr	pc, _irq
	ldr	pc, _fiq
	.endm
```
这里定义了异常向量表 ARM_VECTORS

```
/*
 *************************************************************************
 *
 * Symbol _start is referenced elsewhere, so make it global
 *
 *************************************************************************
 */

.globl _start
```
定义全局函数 _start，为 uboot  代码的起始函数 


```
/*
 *************************************************************************
 *
 * Vectors have their own section so linker script can map them easily
 *
 *************************************************************************
 */

	.section ".vectors", "ax"
```
定义代码段**vectors**



```
#if defined(CONFIG_ENABLE_ARM_SOC_BOOT0_HOOK)
/*
 * Various SoCs need something special and SoC-specific up front in
 * order to boot, allow them to set that in their boot0.h file and then
 * use it here.
 *
 * To allow a boot0 hook to insert a 'special' sequence after the vector
 * table (e.g. for the socfpga), the presence of a boot0 hook supresses
 * the below vector table and assumes that the vector table is filled in
 * by the boot0 hook.  The requirements for a boot0 hook thus are:
 *   (1) defines '_start:' as appropriate
 *   (2) inserts the vector table using ARM_VECTORS as appropriate
 */
#include <asm/arch/boot0.h>

#else

/*
 *************************************************************************
 *
 * Exception vectors as described in ARM reference manuals
 *
 * Uses indirect branch to allow reaching handlers anywhere in memory.
 *
 *************************************************************************
 */

_start:
#ifdef CONFIG_SYS_DV_NOR_BOOT_CFG
	.word	CONFIG_SYS_DV_NOR_BOOT_CFG
#endif
	ARM_VECTORS
#endif /* !defined(CONFIG_ENABLE_ARM_SOC_BOOT0_HOOK) */

/*
 *************************************************************************
 *
 * Indirect vectors table
 *
 * Symbols referenced here must be defined somewhere else
 *
 *************************************************************************
 */

	.globl  _reset
	.globl	_undefined_instruction
	.globl	_software_interrupt
	.globl	_prefetch_abort
	.globl	_data_abort
	.globl	_not_used
	.globl	_irq
	.globl	_fiq
```



参考：
[六、uboot 代码流程分析---start.S](https://www.cnblogs.com/kele-dad/p/8986695.html)