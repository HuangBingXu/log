###### gpio.h

**u-boot\include\asm-generic\gpio.h**

```
/**
 * struct gpio_dev_priv - information about a device used by the uclass
 *						给uclasss使用的一些关于device的informaton
 * The uclass combines all active GPIO devices into a unified numbering
 * scheme. To do this it maintains some private information about each
 * device.
 *
 * To implement driver model support in your GPIO driver, add a probe
 * handler, and set @gpio_count and @bank_name correctly in that handler.
 * This tells the uclass the name of the GPIO bank and the number of GPIOs
 * it contains.
 *
 * @bank_name: Name of the GPIO device (e.g 'a' means GPIOs will be called
 * 'A0', 'A1', etc.
 * @gpio_count: Number of GPIOs in this device
 * @gpio_base: Base GPIO number for this device. For the first active device
 * this will be 0; the numbering for others will follow sequentially so that
 * @gpio_base for device 1 will equal the number of GPIOs in device 0.
 * @name: Array of pointers to the name for each GPIO in this bank. The
 * value of the pointer will be NULL if the GPIO has not been claimed.
 */
struct gpio_dev_priv {
	const char *bank_name;
	unsigned gpio_count;
	unsigned gpio_base;
	char **name;
};
```



```
/**
 * struct struct dm_gpio_ops - Driver model GPIO operations
 *
 * Refer to functions above for description. These function largely copy
 * the old API.
 *
 * This is trying to be close to Linux GPIO API. Once the U-Boot uses the
 * new DM GPIO API, this should be really easy to flip over to the Linux
 * GPIO API-alike interface.
 *
 * Also it would be useful to standardise additional functions like
 * pullup, slew rate and drive strength.
 *
 * gpio_request() and gpio_free() are optional - if NULL then they will
 * not be called.
 *
 * Note that @offset is the offset from the base GPIO of the device. So
 * offset 0 is the device's first GPIO and offset o-1 is the last GPIO,
 * where o is the number of GPIO lines controlled by the device. A device
 * is typically used to control a single bank of GPIOs. Within complex
 * SoCs there may be many banks and therefore many devices all referring
 * to the different IO addresses within the SoC.
 *
 * The uclass combines all GPIO devices together to provide a consistent
 * numbering from 0 to n-1, where n is the number of GPIOs in total across
 * all devices. Be careful not to confuse offset with gpio in the parameters.
 */
struct dm_gpio_ops {
	int (*request)(struct udevice *dev, unsigned offset, const char *label);
	int (*free)(struct udevice *dev, unsigned offset);
	int (*direction_input)(struct udevice *dev, unsigned offset);
	int (*direction_output)(struct udevice *dev, unsigned offset,
				int value);
	int (*get_value)(struct udevice *dev, unsigned offset);
	int (*set_value)(struct udevice *dev, unsigned offset, int value);
	int (*get_open_drain)(struct udevice *dev, unsigned offset);
	int (*set_open_drain)(struct udevice *dev, unsigned offset, int value);
	/**
	 * get_function() Get the GPIO function
	 *
	 * @dev:     Device to check
	 * @offset:  GPIO offset within that device
	 * @return current function - GPIOF_...
	 */
	int (*get_function)(struct udevice *dev, unsigned offset);

	/**
	 * xlate() - Translate phandle arguments into a GPIO description
	 *
	 * This function should set up the fields in desc according to the
	 * information in the arguments. The uclass will have set up:
	 *
	 *   @desc->dev to @dev
	 *   @desc->flags to 0
	 *   @desc->offset to 0
	 *
	 * This method is optional and defaults to gpio_xlate_offs_flags,
	 * which will parse offset and the GPIO_ACTIVE_LOW flag in the first
	 * two arguments.
	 *
	 * Note that @dev is passed in as a parameter to follow driver model
	 * uclass conventions, even though it is already available as
	 * desc->dev.
	 *
	 * @dev:	GPIO device
	 * @desc:	Place to put GPIO description
	 * @args:	Arguments provided in description
	 * @return 0 if OK, -ve on error
	 */
	int (*xlate)(struct udevice *dev, struct gpio_desc *desc,
		     struct ofnode_phandle_args *args);
};
```



```
struct gpio_desc {
	struct udevice *dev;	/* Device, NULL for invalid GPIO */
	unsigned long flags;
#define GPIOD_REQUESTED		(1 << 0)	/* Requested/claimed */
#define GPIOD_IS_OUT		(1 << 1)	/* GPIO is an output */
#define GPIOD_IS_IN		(1 << 2)	/* GPIO is an input */
#define GPIOD_ACTIVE_LOW	(1 << 3)	/* value has active low */
#define GPIOD_IS_OUT_ACTIVE	(1 << 4)	/* set output active */

	uint offset;		/* GPIO offset within the device */
	/*
	 * We could consider adding the GPIO label in here. Possibly we could
	 * use this structure for internal GPIO information.
	 */
};		
```

```
/* State of a GPIO, as reported by get_function() */
enum gpio_func_t {
	GPIOF_INPUT = 0,
	GPIOF_OUTPUT,
	GPIOF_UNUSED,		/* Not claimed */
	GPIOF_UNKNOWN,		/* Not known */
	GPIOF_FUNC,		/* Not used as a GPIO */

	GPIOF_COUNT,
};
```

