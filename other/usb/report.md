###### 短条目

由一字节前缀后面跟上可选的数据组成，可选的数据字节可以为0、1、2、4字节



* 条目前缀

  | D7~D4 | D3~D2 | D1~D0 |
  | ----- | ----- | ----- |
  | bTag  | bTyte | bSize |

  * bTag：该条目具体功能，

    具体需参考HID协议及HID用途表

  * bType：条目类型

    |   0    |    1     |    2     |  3   |
    | :----: | :------: | :------: | :--: |
    | 主条目 | 全局条目 | 局部条目 | 保留 |

  * bSize

    表示后面所跟字节数

  * 

* 数据



#### 条目类型

* 主条目：用来定义报告的数据，或者分组报告的数据

  ```mermaid
  graph TB
  
  A[主条目] --> B[Input输入]
  
  A[主条目] --> C[Output输出]
  
  A[主条目] --> D[Feature特征]
  
  A[主条目] --> E[Collection集合]
  
  A[主条目] --> F[End Collection关集合]
  ```

  

* 全局条目：用来选择用途页，定义数据域的长度、数量、报告ID等，全局条目在出现后对接下来的所有主条目都有效，除非遇到另一个全局条目

  * Usage Page：用途页
  * Logic Minimun：逻辑最小值
  * Logic Maximum：逻辑最大值
  * Physical Minimun：物理最小值
  * Physical Maximum：物理最大值
  * Report Size：数据域大小
  * Report Count：数据域数量
  * Report ID

* 局部条目

