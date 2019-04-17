## STM32 TIM
* 从模式控制单元负责时钟源、触发信号源的选择；控制计数器的启停、复位、门控等
* 时基单元：定时器核心单元。负责时钟源的分频、计数、溢出重装等。
    * 通用定时器、基本定时器
        PSC：分频器
        CNT：计数器
        ARR：自动重装载器
        RCR：重复计数器（高级定时器才有）

* 输入单元：为部分的时钟信号、 捕捉信号、 触发信号提供信号源。
* 比较输出单元：通过对比较寄存器与计数器的数值匹配比较，实现不同输出波形。
*  触发输出单元：输出触发信号给到其它定时器或外设。
* 捕捉比较单元： 是输入捕捉或比较输出的公共执行单元。



基本信号：
* 输入信号
* 时钟信号
* 触发输入信号
* 触发输出信号

事件：
* 更新事件
* 触发事件
* 捕获、比较事件



UEV：update event


CCxIF can be cleared by software by writing it to 0 or by reading the captured data stored in the TIMx_CCRx register.

Reset Mode - Rising edge of the selected trigger input (TRGI) reinitializes the counter and generates an update of the registers.


读定时器计数器的时候，计数器会清零？