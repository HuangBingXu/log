#### source

* level 1

  u-boot-2018.11\arch\arm\dts\stm32mp157c-dk2.dts

```
#include "stm32mp157a-dk1.dts"
#include <dt-bindings/rtc/rtc-stm32.h>
```

* level 2

  * u-boot-2018.11\arch\arm\dts\stm32mp157a-dk1.dts
  * rtc-stm32.h

* level 3 

  in file **stm32mp157a-dk1.dts**

```
#include "stm32mp157c.dtsi"
#include "stm32mp157c-m4-srm.dtsi"
#include "stm32mp157cac-pinctrl.dtsi"
#include <dt-bindings/gpio/gpio.h>
#include <dt-bindings/input/input.h>
#include <dt-bindings/mfd/st,stpmic1.h>
```

