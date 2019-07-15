1.

```
ENTRY(_start)
SECTIONS
{
	. = 0x00000000;

	. = ALIGN(4);
	.text :
	{
		__image_copy_start = .;
		*(.vectors)
		CPUDIR/start.o (.text*)
		*(.text*)
		*(.glue*)
	}
```



**ENTRY(_start)**表示程序入口为**_start**,该入口在文件**vectors.S**中，定义了些异常向量

上面代码中第5行：
>. = 0x00000000;                   

定义 **.** 变量为0x00000000

第10行：
>		__image_copy_start = .;

给变量 **__image_copy_start** 赋值，


第11行：
>		*(.vectors)
这段内存存放的代码段为**vectors**，具体在：**u-boot-2018.11\arch\arm\lib\vectors.S**中定义：
```
.globl _start

/*
 *************************************************************************
 *
 * Vectors have their own section so linker script can map them easily
 *
 *************************************************************************
 */

	.section ".vectors", "ax"
```

12行：
>		CPUDIR/start.o (.text*)
表示该代码段内容为start.s中的内容，具体在：**u-boot-2018.11\arch\arm\cpu\armv7\start.S**





LDS语法：

 OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
/*指定输出可执行文件是elf格式,32位ARM指令,小端*/

OUTPUT_ARCH(arm)
/*指定输出可执行文件的平台为ARM*/

ENTRY(_start)
/*指定输出可执行文件的起始代码段为_start*/
ENTRY(symbol): 設定某個symbol為程式執行的第一個指令起始點