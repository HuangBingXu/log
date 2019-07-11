1、设备状态

* 开放模式：**默认状态**，认证不是强制的，就算认证错误，也不会停止运行FSBL（First  Stage Boot loader）

* 关闭状态：通过写OTP WORD0 bit 6开启，认证失败就不会再允许FSBL，

* RMA state： RMA（Return Material Authorization）



[Image signing](https://wiki.st.com/stm32mpu/wiki/STM32MP15_secure_boot#STM32_Header)：系统二进制签名

![](https://wiki.st.com/stm32mpu/nsfr_img_auth.php/4/4c/STM32_header.png)

 The [ROM code](https://wiki.st.com/stm32mpu/wiki/STM32MP15_ROM_code_overview) uses 9 Kbytes located at the beginning of the SYSRAM to store its read and write data.(from [SYSRAM_internal_memory](https://wiki.st.com/stm32mpu/wiki/SYSRAM_internal_memory))

The [ROM code](https://wiki.st.com/stm32mpu/wiki/STM32MP15_ROM_code_overview) loads the [FSBL](https://wiki.st.com/stm32mpu/wiki/Boot_chains_overview) just after the boot context, into the remaining 247 Kbytes of SYSRAM, and eventually branches the Cortex®-A7 core 0 execution to this [FSBL](https://wiki.st.com/stm32mpu/wiki/Boot_chains_overview).

The [FSBL](https://wiki.st.com/stm32mpu/wiki/Boot_chains_overview) code can use the whole SYSRAM, but it must take care not to overwrite the boot context before taking it into account.