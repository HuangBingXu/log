## RC5
*   14-bit,bit's len 1.778ms,
*    bi-phase modulation

RC5数据帧：
* 起始位 (S)： 长度为 1 位，始终为逻辑 1。
* 字段位 (F)： 长度为 1 位，表示发送的命令位于低位字段（逻辑 1 = 十进制数 0 到 63）
还是高位字段（逻辑 0 = 十进制数 64 到 127）。该字段位是后来增加的，因为人们意
识到每个设备 64 条命令是不够的。以前，该字段位与起始位结合在一起。许多设备仍
在使用这种原始体系。
* 控制位或切换位 (C)： 长度为 1 位，每次按下按钮时切换。这使得接收设备可以区分两
次连续的按钮按下操作（例如“1”、“1”代表“11”）
* 地址： 长度为 5 位，可选择 32 种可能系统中的一种。
* 命令： 长度为 6 位（与字段位结合使用），表示 128 种可能的 RC5 命令中的一种。