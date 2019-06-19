1、什么是STM32MPU             
    [STM32MPU](https://www.st.com/en/microcontrollers-microprocessors/stm32-arm-cortex-mpus.html#overview)是ST推出的Cortex-A7 + Cortex-M4多核异构处理器             

* STM32MPU151是单核A7+M4，、STM32MPU153、STM32MPU157是双核A7+M4。             
* A7核最高可以跑到650MHZ，M4核最高可以达到209MHZ，

2、开发工具        
硬件
目前为止（20190618），能够在官网找到的开发板有4款,分两类：
* STM32MP15 Evaluation boards：[STM32MP157A-DK1](https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/stm32mp157a-dk1.html)、[STM32MP157C-DK2](https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/stm32mp157c-dk2.html)
* STM32MP15 Discovery kits：[STM32MP157A-EV1](https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-eval-boards/stm32mp157a-ev1.html)、  [STM32MP157C-EV1](https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-eval-boards/stm32mp157c-ev1.html)

软件

M4核方面，ST提供了[Enhanced STM32Cube](https://www.st.com/content/st_com/en/stm32cube-ecosystem.html)一整套开发工具,

* 代码生成工具：[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
* IDE: [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html)
* 烧录软件：[STM32CubeProg](https://www.st.com/en/development-tools/stm32cubeprog.html)
* 调试工具：[STM32CubeMonitor family of tools](https://www.st.com/content/st_com/en/stm32cube-ecosystem.html#DataTables_Table_0)

A核方面，ST提供了[OpenSTLinux](https://www.st.com/en/embedded-software/stm32-mpu-openstlinux-distribution.html#overview)

根据不同需求，ST提供了3类开发包：               
* [STM32MP1Starter](https://www.st.com/content/st_com/en/products/embedded-software/mcu-mpu-embedded-software/stm32-embedded-software/stm32-mpu-openstlinux-distribution/stm32mp1starter.html#overview)，
这是ST为他们的开发板提供的OpenSTLinux的二进制文件，用来快速体验、评估STM32MPU系列处理器。              
相关wiki:
    * [STM32MP15 Discovery kits - Starter Package](https://wiki.st.com/stm32mpu/wiki/STM32MP15_Discovery_kits_-_Starter_Package)
    * [STM32MP15 Evaluation boards - Starter Package](https://wiki.st.com/stm32mpu/wiki/STM32MP15_Discovery_kits_-_Starter_Package)
* [Developer Package]()：提供开发工具，可以应用添加到
* []()

需要哪一种开发包呢，可以参考[这里](https://wiki.st.com/stm32mpu/wiki/Which_Package_better_suits_your_needs)


## SoftWare

[TF-A overview](https://wiki.st.com/stm32mpu/wiki/TF-A_overview)
[OP-TEE overview](https://wiki.st.com/stm32mpu/wiki/OP-TEE_overview)