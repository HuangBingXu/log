 OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
/*指定输出可执行文件是elf格式,32位ARM指令,小端*/

OUTPUT_ARCH(arm)
/*指定输出可执行文件的平台为ARM*/

ENTRY(_start)
/*指定输出可执行文件的起始代码段为_start*/
ENTRY(symbol): 設定某個symbol為程式執行的第一個指令起始點