##### 主引导记录（MBR：Master Boot Record）

是[计算机](https://zh.wikipedia.org/wiki/计算机)开机后访问[硬盘](https://zh.wikipedia.org/wiki/硬盘)时所必须要读取的首个扇区

在MBR硬盘中，分区信息直接存储于[主引导记录](https://zh.wikipedia.org/wiki/主引导记录)（MBR）中（主引导记录中还存储着系统的[引导程序](https://zh.wikipedia.org/wiki/引导程序)）



### 全局唯一标识分区表（GPT：GUID Partition Table） 

实体[硬盘](https://zh.wikipedia.org/wiki/硬盘)的[分区表](https://zh.wikipedia.org/wiki/分区表)的结构布局的标准

GPT硬盘中，分区表的位置信息储存在GPT头中。但出于[兼容性](https://zh.wikipedia.org/wiki/兼容性)考虑，硬盘的第一个扇区仍然用作MBR，之后才是GPT头。

为了减少分区表损坏的风险，GPT在硬盘最后保存了一份分区表的副本。































[逻辑区块地址](https://zh.wikipedia.org/wiki/邏輯區塊位址)（LBA）