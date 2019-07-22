#### Block devie



### part_driver

```
/* Declare a new U-Boot partition 'driver' */
#define U_BOOT_PART_TYPE(__name)					\
	ll_entry_declare(struct part_driver, __name, part_driver)
```





> int spl_mmc_load_image(struct spl_image_info **spl_image*,  struct spl_boot_device **bootdev*) 

```
#ifdef CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_USE_PARTITION
static int mmc_load_image_raw_partition(struct spl_image_info *spl_image,
					struct mmc *mmc, int partition)
{
	disk_partition_t info;
	int err;

#ifdef CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_USE_PARTITION_TYPE
	int type_part;
	/* Only support MBR so DOS_ENTRY_NUMBERS */
	for (type_part = 1; type_part <= DOS_ENTRY_NUMBERS; type_part++) {
		err = part_get_info(mmc_get_blk_desc(mmc), type_part, &info);
		if (err)
			continue;
		if (info.sys_ind == 
			CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_PARTITION_TYPE) {
			partition = type_part;
			break;
		}
	}
#endif

	err = part_get_info(mmc_get_blk_desc(mmc), partition, &info);
	if (err) {
#ifdef CONFIG_SPL_LIBCOMMON_SUPPORT
		puts("spl: partition error\n");
#endif
		return -1;
	}

#ifdef CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_USE_SECTOR
	return mmc_load_image_raw_sector(spl_image, mmc,
			info.start + CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_SECTOR);
#else
	return mmc_load_image_raw_sector(spl_image, mmc, info.start);
#endif
}
#endif
```



