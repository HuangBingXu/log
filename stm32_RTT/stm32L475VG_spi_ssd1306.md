尝试下在RT-Thread驱动0.96 寸OLED，驱动器是SSD1306，我手上的模块是SPI接口，如下图：

需要的接口有：VCC GND D0 D1 RST DC CS，
其中D0 D1 CS分别是SPI接口的SCK、MOSI、CS，RST是SSD1306复位脚，DC是命令数据选择脚，

### 配置SPI总线
配置之前，存在的设备或总线有：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/27BC59033EE048A0AC9199DACDBD5879/10852)

从上图可以看到只有UART跟PIN设备，接下来开始配置SPI总线，

1. 因为新的BSP使用HAL库，需要在cubeMX中初始化SPI，使能SPI，如下图，然后重新生成代码，

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/B8F1C559EFD64F899624E9236A90BDBB/10859)


2. 在RT——Thread中使用SPI接口，还需要在menuconfig配置SPI，如下图：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/7E016F50DC7D430D842CF3D911AA24C1/10849)

配置完，编译并烧录到板子上，看下SPI总线有没有成功创建，执行结果如下图：

![image](https://note.youdao.com/yws/public/resource/919c6707afc9d8666b0482b3b9c6ab85/xmlnote/7F9CCE00B07143418F8E57F8F85E3D64/10850)

可以看出，跟配置之前相比，多了个spi1,


## 实现相关代码

1、实现相关硬件的初始化：SPI、IO。



```
#define SSD1306_DC_PIN  GET_PIN(B, 2)
#define SSD1306_RES_PIN GET_PIN(A, 4)
static struct rt_spi_device *spi_dev_lcd;

static int rt_hw_ssd1306_config(void)
{
    __HAL_RCC_GPIOA_CLK_ENABLE();
    rt_hw_spi_device_attach("spi1", "spi10", GPIOA, GPIO_PIN_15);

    spi_dev_lcd = (struct rt_spi_device *)rt_device_find("spi10");

    /* config spi */
    {
        struct rt_spi_configuration cfg;
        cfg.data_width = 8;
        cfg.mode = RT_SPI_MASTER | RT_SPI_MODE_3 | RT_SPI_MSB;
        cfg.max_hz = 42 * 1000 * 1000; /* 42M,SPI max 42MHz,lcd 4-wire spi */

        rt_spi_configure(spi_dev_lcd, &cfg);
    }

    rt_pin_mode(SSD1306_DC_PIN, PIN_MODE_OUTPUT);
    rt_pin_mode(SSD1306_RES_PIN, PIN_MODE_OUTPUT);

    return RT_EOK;
}

```

挂载 SPI 从设备到SPI总线设备上 




2.  然后分别实现SSD1306写数据、写命令函数：

```
static rt_err_t ssd1306_write_cmd(const rt_uint8_t cmd)
{
    rt_size_t len;

    rt_pin_write(SSD1306_DC_PIN, PIN_LOW);

    len = rt_spi_send(spi_dev_lcd, &cmd, 1);

    if (len != 1)
    {
        LOG_I("ssd1306_write_cmd error. %d", len);
        return -RT_ERROR;
    }
    else
    {
        return RT_EOK;
    }
}

static rt_err_t ssd1306_write_data(const rt_uint8_t data)
{
    rt_size_t len;

    rt_pin_write(SSD1306_DC_PIN, PIN_HIGH);

    len = rt_spi_send(spi_dev_lcd, &data, 1);

    if (len != 1)
    {
        LOG_I("ssd1306_write_data error. %d", len);
        return -RT_ERROR;
    }
    else
    {
        return RT_EOK;
    }
}
```

3. 定义个数组，用作SSD1306显示缓存，并实现把缓存写入SSD1306的函数：

```
uint8_t SSD1306_GRAM[128][8];

void ssd1306_refresh_gram(void)
{
	uint8_t i,n;		    
	for(i=0;i<8;i++)  
	{  
		ssd1306_write_cmd (0xb0+i);   
		ssd1306_write_cmd (0x00);      
		ssd1306_write_cmd (0x10);      
		for(n=0;n<128;n++)
            ssd1306_write_data(SSD1306_GRAM[n][i]); 
	}   
}


```

4. 实现请屏幕跟把所有像素都点亮的函数：
```
void ssd1306_clear(void)  
{  
	uint8_t i,n;  
	for(i=0;i<8;i++)for(n=0;n<128;n++)SSD1306_GRAM[n][i]=0X00;  
	    ssd1306_refresh_gram();
}
FINSH_FUNCTION_EXPORT(ssd1306_clear, clear ssd136 screan);
MSH_CMD_EXPORT(ssd1306_clear,  clear ssd136 screan);

void ssd1306_fill(void)  
{  
	uint8_t i,n;  
	for(i=0;i<8;i++)for(n=0;n<128;n++)SSD1306_GRAM[n][i]=0Xff;  
	    ssd1306_refresh_gram();
}
FINSH_FUNCTION_EXPORT(ssd1306_fill, fill ssd136 screan);
MSH_CMD_EXPORT(ssd1306_fill, fill ssd136 screan);
```

5. 最后实现SSD1306初始化函数，并把所有像素点亮，测试驱动是不是成功的：

```
static int rt_hw_ssd1306_init(void)
{
    ssd1306_gpio_init();

	ssd1306_write_cmd(0xAE); 
	ssd1306_write_cmd(0xD5); 
	ssd1306_write_cmd(80);  
	ssd1306_write_cmd(0xA8);
	ssd1306_write_cmd(0X3F);
	ssd1306_write_cmd(0xD3); 
	ssd1306_write_cmd(0X00);

	ssd1306_write_cmd(0x40); 
													    
	ssd1306_write_cmd(0x8D); 
	ssd1306_write_cmd(0x14); 
	ssd1306_write_cmd(0x20); 
	ssd1306_write_cmd(0x02); 
	ssd1306_write_cmd(0xA1); 
	ssd1306_write_cmd(0xC0);
	ssd1306_write_cmd(0xDA); 
	ssd1306_write_cmd(0x12); 
		 
	ssd1306_write_cmd(0x81); 
	ssd1306_write_cmd(0xEF);
	ssd1306_write_cmd(0xD9); 
	ssd1306_write_cmd(0xf1); 
	ssd1306_write_cmd(0xDB); 
	ssd1306_write_cmd(0x30); 

	ssd1306_write_cmd(0xA4); 
	ssd1306_write_cmd(0xA6); 
	ssd1306_write_cmd(0xAF); 

    ssd1306_clear();

    return RT_EOK;
}
INIT_DEVICE_EXPORT(rt_hw_ssd1306_init);
```

### 修改Kconfig文件
驱动测试成功后，修改下Kconfig，在 **board** 目录下的 **Kconfig** 的 **menu "Onboard Peripheral Drivers"**添加如下：
```
       config BSP_USING_SSD1306
        bool "Enable SSD1306 (spi1)"
        select BSP_USING_SPI
        select BSP_USING_SPI1
        default n
```
参考文档：
1. [SPI设备](https://www.rt-thread.org/document/site/programming-manual/device/spi/spi/
)
