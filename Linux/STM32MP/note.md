执行make stm32mp15_basic_defconfig编译U-boot的时候碰到这个问题：
```
  HOSTCC  scripts/basic/fixdep
  HOSTCC  scripts/kconfig/conf.o
  YACC    scripts/kconfig/zconf.tab.c
/bin/sh: 1: bison: not found
scripts/Makefile.lib:228: recipe for target 'scripts/kconfig/zconf.tab.c' failed
make[1]: *** [scripts/kconfig/zconf.tab.c] Error 127
Makefile:496: recipe for target 'stm32mp15_basic_defconfig' failed
make: *** [stm32mp15_basic_defconfig] Error 2
wyl@wyl-ub:~/STM32MPU_workspace/STM32MP15-Ecosystem-v1.0.0/u-boot-stm32mp-2018.11-r0/u-boot-2018.11$ make stm32mp15_trusted_defconfig  YACC    scripts/kconfig/zconf.tab.c
/bin/sh: 1: bison: not found
scripts/Makefile.lib:228: recipe for target 'scripts/kconfig/zconf.tab.c' failed
make[1]: *** [scripts/kconfig/zconf.tab.c] Error 127
Makefile:496: recipe for target 'stm32mp15_trusted_defconfig' failed
make: *** [stm32mp15_trusted_defconfig] Error 2
```

解决方法：
> sudo apt-get install bison


