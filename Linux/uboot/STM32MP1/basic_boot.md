按照[U-Boot.README.HOW_TO.txt](https://wiki.st.com/stm32mpu/nsfr_img_auth.php/5/57/U-Boot.README.HOW_TO.txt)，
编译：
```
make stm32mp15_basic_defconfig
make DEVICE_TREE=stm32mp157c-dk2 all
```

然后更新：
```
6.2.1. Basic boot chain
* u-boot-spl.stm32-*
  Copy the binary on the dedicated partition, on SDCARD/USB disk the partition
  "fsbl1" is the partition 1:
  - SDCARD: /dev/mmcblkXp1 (where X is the instance number)
  - SDCARD via USB reader: /dev/sdX1 (where X is the instance number)
  dd if=<U-Boot SPL file> of=/dev/<device partition> bs=1M conv=fdatasync

* u-boot*.img
  Copy the binary on the dedicated partition, on SDCARD/USB disk the partition
  "ssbl" is the partition 4:
  - SDCARD: /dev/mmcblkXp3 (where X is the instance number)
  - SDCARD via USB reader: /dev/sdX3 (where X is the instance number)
  dd if=<U-Boot image file> of=/dev/<device partition> bs=1M conv=fdatasync
  ```

```
wyl@wyl-ThinkPad-X240:~$ ls -l /dev/disk/by-partlabel/
total 0
lrwxrwxrwx 1 root root 10 6月  20 11:21 bootfs -> ../../sdb4
lrwxrwxrwx 1 root root 10 6月  20 11:21 fsbl1 -> ../../sdb1
lrwxrwxrwx 1 root root 10 6月  20 11:21 fsbl2 -> ../../sdb2
lrwxrwxrwx 1 root root 10 6月  20 11:21 rootfs -> ../../sdb6
lrwxrwxrwx 1 root root 10 6月  20 11:21 ssbl -> ../../sdb3
lrwxrwxrwx 1 root root 10 6月  20 11:21 userfs -> ../../sdb7
lrwxrwxrwx 1 root root 10 6月  20 11:21 vendorfs -> ../../sdb5

```
sudo dd if=u-boot-spl.stm32 of=/dev/sdb1 bs=1M conv=fdatasync

sudo dd if=u-boot-dtb.img  of=/dev/sdb3  bs=1M conv=fdatasync


更新u-boot后，启动log:

```

U-Boot SPL 2018.11-stm32mp-r2 (Jun 20 2019 - 11:26:02 +0800)
Model: STMicroelectronics STM32MP157C-DK2 Discovery Board
RAM: DDR3-1066/888 bin G 1x4Gb 533MHz v1.41
Trying to boot from MMC1


U-Boot 2018.11-stm32mp-r2 (Jun 20 2019 - 11:26:02 +0800)

CPU: STM32MP157CAC Rev.B
Model: STMicroelectronics STM32MP157C-DK2 Discovery Board
Board: stm32mp1 in basic mode (st,stm32mp157c-dk2)
U-Boot simple example
Board: MB1272 Var2 Rev.C-01
       Watchdog enabled
DRAM:  512 MiB
Clocks:
- MPU : 650 MHz
- MCU : 208.878 MHz
- AXI : 266.500 MHz
- PER : 24 MHz
- DDR : 533 MHz

*******************************************
*   WARNING 500mA power supply detected   *
* Current too low, use a 3A power supply! *
*******************************************

NAND:  0 MiB
MMC:   STM32 SDMMC2: 0, STM32 SDMMC2: 1
In:    serial
Out:   serial
Err:   serial
Net:   eth0: ethernet@5800a000
Boot over mmc0!
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:4...
Found U-Boot script /boot.scr.uimg
1553 bytes read in 1 ms (1.5 MiB/s)
## Executing script at c4100000
Scanning mmc 0:4...
Found /mmc0_stm32mp157c-dk2_extlinux/extlinux.conf
Retrieving file: /mmc0_stm32mp157c-dk2_extlinux/extlinux.conf
616 bytes read in 1 ms (601.6 KiB/s)
Retrieving file: /mmc0_stm32mp157c-dk2_extlinux/../splash.bmp
46180 bytes read in 2 ms (22 MiB/s)
Select the boot mode
1:      stm32mp157c-dk2-sdcard
2:      stm32mp157c-dk2-a7-examples-sdcard
3:      stm32mp157c-dk2-m4-examples-sdcard
Enter choice: 1:        stm32mp157c-dk2-sdcard
Retrieving file: /uImage
6569168 bytes read in 289 ms (21.7 MiB/s)
append: root=/dev/mmcblk0p6 rootwait rw console=ttySTM0,115200
Retrieving file: /stm32mp157c-dk2.dtb
69510 bytes read in 4 ms (16.6 MiB/s)
## Booting kernel from Legacy Image at c2000000 ...
   Image Name:   Linux-4.19.9
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    6569104 Bytes = 6.3 MiB
   Load Address: c2000040
   Entry Point:  c2000040
   Verifying Checksum ... OK
## Flattened Device Tree blob at c4000000
   Booting using the fdt blob at 0xc4000000
   XIP Kernel Image ... OK
   Using Device Tree in place at c4000000, end c4013f85

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.19.9 (oe-user@oe-host) (gcc version 8.2.0 (GCC)) #1 SMP PREEMPT Thu Dec 13 08:16:23 UTC 2018
[    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
[    0.000000] CPU: div instructions available: patching division code
[    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
[    0.000000] OF: fdt: Machine model: STMicroelectronics STM32MP157C-DK2 Discovery Board
[    0.000000] Memory policy: Data cache writealloc
[    0.000000] Reserved memory: created DMA memory pool at 0x10000000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node mcuram2@0x10000000, compatible id shared-dma-pool
[    0.000000] Reserved memory: created DMA memory pool at 0x10040000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node vdev0vring0@10040000, compatible id shared-dma-pool
[    0.000000] Reserved memory: created DMA memory pool at 0x10042000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node vdev0vring1@10042000, compatible id shared-dma-pool
[    0.000000] Reserved memory: created DMA memory pool at 0x10044000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node vdev0buffer@10044000, compatible id shared-dma-pool
[    0.000000] Reserved memory: created DMA memory pool at 0x30000000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node mcuram@0x30000000, compatible id shared-dma-pool
[    0.000000] Reserved memory: created DMA memory pool at 0x38000000, size 0 MiB
[    0.000000] OF: reserved mem: initialized node retram@0x38000000, compatible id shared-dma-pool
[    0.000000] cma: Reserved 128 MiB at 0xd4000000
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.0 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: Trusted OS migration not required
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] random: get_random_bytes called from start_kernel+0xa0/0x494 with crng_init=0
[    0.000000] percpu: Embedded 17 pages/cpu @(ptrval) s40204 r8192 d21236 u69632
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 113680
[    0.000000] Kernel command line: root=/dev/mmcblk0p6 rootwait rw console=ttySTM0,115200
[    0.000000] Dentry cache hash table entries: 65536 (order: 6, 262144 bytes)
[    0.000000] Inode-cache hash table entries: 32768 (order: 5, 131072 bytes)
[    0.000000] Memory: 306144K/458752K available (10240K kernel code, 816K rwdata, 2860K rodata, 1024K init, 208K bss, 21536K reserved, 131072K cma-reserved, 0K highmem)
[    0.000000] Virtual kernel memory layout:
[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
[    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
[    0.000000]     vmalloc : 0xdc800000 - 0xff800000   ( 560 MB)
[    0.000000]     lowmem  : 0xc0000000 - 0xdc000000   ( 448 MB)
[    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
[    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
[    0.000000]       .text : 0x(ptrval) - 0x(ptrval)   (11232 kB)
[    0.000000]       .init : 0x(ptrval) - 0x(ptrval)   (1024 kB)
[    0.000000]       .data : 0x(ptrval) - 0x(ptrval)   ( 817 kB)
[    0.000000]        .bss : 0x(ptrval) - 0x(ptrval)   ( 209 kB)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
[    0.000000]  Tasks RCU enabled.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000000] /soc/interrupt-controller@5000d000: bank0
[    0.000000] /soc/interrupt-controller@5000d000: bank1
[    0.000000] /soc/interrupt-controller@5000d000: bank2
[    0.000000] arch_timer: cp15 timer(s) running at 24.00MHz (virt).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[    0.000009] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000027] Switching to timer-based delay loop, resolution 41ns
[    0.001911] Console: colour dummy device 80x30
[    0.001963] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=240000)
[    0.001987] pid_max: default: 32768 minimum: 301
[    0.002225] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.002246] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.003255] CPU: Testing write buffer coherency: ok
[    0.003759] CPU0: update cpu_capacity 1024
[    0.003781] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
[    0.059779] Setting up static identity map for 0xc0100000 - 0xc0100060
[    0.079767] rcu: Hierarchical SRCU implementation.
[    0.119917] smp: Bringing up secondary CPUs ...
[    0.200275] CPU1: update cpu_capacity 1024
[    0.200287] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
[    0.200494] smp: Brought up 1 node, 2 CPUs
[    0.200524] SMP: Total of 2 processors activated (96.00 BogoMIPS).
[    0.200534] CPU: All CPU(s) started in SVC mode.
[    0.201665] devtmpfs: initialized
[    0.226850] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
[    0.227367] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.227402] futex hash table entries: 512 (order: 3, 32768 bytes)
[    0.233486] pinctrl core: initialized pinctrl subsystem
[    0.235615] NET: Registered protocol family 16
[    0.242960] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.245428] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
[    0.245449] hw-breakpoint: maximum watchpoint size is 8 bytes.
[    0.245740] Serial: AMBA PL011 UART driver
[    0.247920] stm32-pm-domain pm_domain: domain core-ret-power-domain registered
[    0.247953] stm32-pm-domain pm_domain: subdomain core-power-domain registered
[    0.247969] stm32-pm-domain pm_domain: domains probed
[    0.263441] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOA bank added
[    0.263800] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOB bank added
[    0.264093] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOC bank added
[    0.264361] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOD bank added
[    0.264634] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOE bank added
[    0.264908] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOF bank added
[    0.265168] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOG bank added
[    0.265451] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOH bank added
[    0.265707] stm32mp157-pinctrl soc:pin-controller@50002000: GPIOI bank added
[    0.265911] stm32mp157-pinctrl soc:pin-controller@50002000: Pinctrl STM32 initialized
[    0.266772] stm32mp157-pinctrl soc:pin-controller-z@54004000: GPIOZ bank added
[    0.266800] stm32mp157-pinctrl soc:pin-controller-z@54004000: Pinctrl STM32 initialized
[    0.286435] stm32-mdma 58000000.dma: STM32 MDMA driver registered
[    0.291637] SCSI subsystem initialized
[    0.292409] usbcore: registered new interface driver usbfs
[    0.292498] usbcore: registered new interface driver hub
[    0.292640] usbcore: registered new device driver usb
[    0.292951] pps_core: LinuxPPS API ver. 1 registered
[    0.292965] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.292998] PTP clock support registered
[    0.293283] EDAC MC: Ver: 3.0.0
[    0.294177] Advanced Linux Sound Architecture Driver Initialized.
[    0.295774] clocksource: Switched to clocksource arch_sys_counter
[    0.389650] NET: Registered protocol family 2
[    0.390726] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes)
[    0.390778] TCP established hash table entries: 4096 (order: 2, 16384 bytes)
[    0.390847] TCP bind hash table entries: 4096 (order: 3, 32768 bytes)
[    0.390944] TCP: Hash tables configured (established 4096 bind 4096)
[    0.391094] UDP hash table entries: 256 (order: 1, 8192 bytes)
[    0.391140] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)
[    0.391627] NET: Registered protocol family 1
[    0.392503] RPC: Registered named UNIX socket transport module.
[    0.392525] RPC: Registered udp transport module.
[    0.392536] RPC: Registered tcp transport module.
[    0.392547] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.393623] hw perfevents: enabled with armv7_cortex_a7 PMU driver, 5 counters available
[    0.395883] Initialise system trusted keyrings
[    0.396272] workingset: timestamp_bits=14 max_order=17 bucket_order=3
[    0.407085] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.408239] NFS: Registering the id_resolver key type
[    0.408290] Key type id_resolver registered
[    0.408303] Key type id_legacy registered
[    0.408525] ntfs: driver 2.1.32 [Flags: R/O].
[    0.409017] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    0.409951] fuse init (API version 7.27)
[    0.410641] pstore: using deflate compression
[    0.413517] NET: Registered protocol family 38
[    0.413546] Key type asymmetric registered
[    0.413560] Asymmetric key parser 'x509' registered
[    0.413657] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.413674] io scheduler noop registered
[    0.413686] io scheduler deadline registered
[    0.413950] io scheduler cfq registered (default)
[    0.413966] io scheduler mq-deadline registered
[    0.413978] io scheduler kyber registered
[    0.415288] stm32-usbphyc 5a006000.usbphyc: Linked as a consumer to regulator.1
[    0.415431] stm32-usbphyc 5a006000.usbphyc: Linked as a consumer to regulator.2
[    0.415559] stm32-usbphyc 5a006000.usbphyc: Dropping the link to regulator.2
[    0.415671] stm32-usbphyc 5a006000.usbphyc: Dropping the link to regulator.1
[    0.420515] stm32-dma 48000000.dma: STM32 DMA driver registered
[    0.422304] stm32-dma 48001000.dma: STM32 DMA driver registered
[    0.501947] STM32 USART driver initialized
[    0.503300] 4000e000.serial: ttySTM3 at MMIO 0x4000e000 (irq = 25, base_baud = 4000000) is a stm32-usart
[    0.503600] serial serial0: tty port ttySTM3 registered
[    0.503660] stm32-usart 4000e000.serial: interrupt mode used for rx (no dma)
[    0.503679] stm32-usart 4000e000.serial: interrupt mode used for tx (no dma)
[    0.504887] 40010000.serial: ttySTM0 at MMIO 0x40010000 (irq = 27, base_baud = 4000000) is a stm32-usart
[    1.451009] console [ttySTM0] enabled
[    1.455215] stm32-usart 40010000.serial: interrupt mode used for rx (no dma)
[    1.461728] stm32-usart 40010000.serial: interrupt mode used for tx (no dma)
[    1.476538] stm32-display-dsi 5a000000.dsi: Linked as a consumer to regulator.2
[    1.485729] panel-orisetech-otm8009a 5a000000.dsi.0: 5a000000.dsi.0 supply power not found, using dummy regulator
[    1.494789] panel-orisetech-otm8009a 5a000000.dsi.0: Linked as a consumer to regulator.0
[    1.518202] brd: module loaded
[    1.532489] loop: module loaded
[    1.540437] libphy: Fixed MDIO Bus: probed
[    1.544485] CAN device driver interface
[    1.549415] stm32-dwmac 5800a000.ethernet: PTP uses main clock
[    1.553808] stm32-dwmac 5800a000.ethernet: no reset control found
[    1.560050] stm32-dwmac 5800a000.ethernet: No phy clock provided...
[    1.567298] stm32-dwmac 5800a000.ethernet: User ID: 0x40, Synopsys ID: 0x42
[    1.573168] stm32-dwmac 5800a000.ethernet:   DWMAC4/5
[    1.578207] stm32-dwmac 5800a000.ethernet: DMA HW capability register supported
[    1.585461] stm32-dwmac 5800a000.ethernet: RX Checksum Offload Engine supported
[    1.592886] stm32-dwmac 5800a000.ethernet: TX Checksum insertion supported
[    1.599712] stm32-dwmac 5800a000.ethernet: Wake-Up On Lan supported
[    1.605984] stm32-dwmac 5800a000.ethernet: TSO supported
[    1.611285] stm32-dwmac 5800a000.ethernet: TSO feature enabled
[    1.617155] stm32-dwmac 5800a000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    1.625218] libphy: stmmac: probed
[    1.631261] pegasus: v0.9.3 (2013/04/25), Pegasus/Pegasus II USB Ethernet driver
[    1.637404] usbcore: registered new interface driver pegasus
[    1.642970] usbcore: registered new interface driver asix
[    1.648466] usbcore: registered new interface driver ax88179_178a
[    1.654439] usbcore: registered new interface driver cdc_ether
[    1.660339] usbcore: registered new interface driver smsc75xx
[    1.666093] usbcore: registered new interface driver smsc95xx
[    1.671791] usbcore: registered new interface driver net1080
[    1.677525] usbcore: registered new interface driver cdc_subset
[    1.683387] usbcore: registered new interface driver zaurus
[    1.689039] usbcore: registered new interface driver cdc_ncm
[    1.695890] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.701170] ehci-platform: EHCI generic platform driver
[    1.706955] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.712619] ohci-platform: OHCI generic platform driver
[    1.718574] usbcore: registered new interface driver usb-storage
[    1.728707] stm32_rtc 5c004000.rtc: rtc core: registered 5c004000.rtc as rtc0
[    1.734846] stm32_rtc 5c004000.rtc: Date/Time must be initialized
[    1.740612] stm32_rtc 5c004000.rtc: registered rev:1.2
[    1.746287] i2c /dev entries driver
[    1.769894] stm32f7-i2c 40012000.i2c: can't use DMA
[    1.777094] sii902x 0-0039: Failed to get supply 'iovcc': -517
[    1.782451] stm32f7-i2c 40012000.i2c: STM32F7 I2C-0 bus adapter
[    1.808375] stm32f7-i2c 5c002000.i2c: can't use DMA
[    1.814246] typec_stusb 1-0028: STUSB driver registered
[    1.819939] stpmic1 1-0033: PMIC Chip Version: 0x10
[    1.829108] BUCK1: supplied by regulator-dummy
[    1.836163] BUCK2: supplied by regulator-dummy
[    1.842596] BUCK3: supplied by regulator-dummy
[    1.849482] BUCK4: supplied by regulator-dummy
[    1.856038] LDO1: supplied by v3v3
[    1.863626] LDO2: supplied by regulator-dummy
[    1.870412] LDO3: supplied by vdd_ddr
[    1.876533] LDO4: supplied by regulator-dummy
[    1.881044] LDO5: supplied by regulator-dummy
[    1.887837] LDO6: supplied by v3v3
[    1.893650] VREF_DDR: supplied by regulator-dummy
[    1.900166] BOOST: supplied by regulator-dummy
[    1.904314] VBUS_OTG: supplied by bst_out
[    1.908386] SW_OUT: supplied by bst_out
[    1.913640] random: fast init done
[    1.917484] input: pmic_onkey as /devices/platform/soc/5c002000.i2c/i2c-1/1-0033/5c002000.i2c:stpmic@33:onkey/input/input0
[    1.927747] stm32f7-i2c 5c002000.i2c: STM32F7 I2C-1 bus adapter
[    1.936891] stm_thermal 50028000.thermal: stm_thermal_probe: Driver initialized successfully
[    1.947613] mmci-pl18x 58005000.sdmmc: Linked as a consumer to regulator.8
[    1.953195] mmci-pl18x 58005000.sdmmc: mmc0: PL180 manf 53 rev2 at 0x58005000 irq 58,0 (pio)
[    1.990609] mmci-pl18x 58007000.sdmmc: allocated mmc-pwrseq
[    1.995093] mmci-pl18x 58007000.sdmmc: Linked as a consumer to regulator.8
[    2.002939] mmci-pl18x 58007000.sdmmc: mmc1: PL180 manf 53 rev1 at 0x58007000 irq 59,0 (pio)
[    2.037078] sdhci: Secure Digital Host Controller Interface driver
[    2.042891] sdhci: Copyright(c) Pierre Ossman
[    2.046275] Synopsys Designware Multimedia Card Interface Driver
[    2.052961] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.060920] ledtrig-cpu: registered to indicate activity on CPUs
[    2.066824] usbcore: registered new interface driver usbhid
[    2.071145] usbhid: USB HID core driver
[    2.074937] mmc0: host does not support reading read-only switch, assuming write-enable
[    2.084850] stm32-ipcc 4c001000.mailbox: ipcc rev:1.0 enabled, 6 chans, proc 0
[    2.091864] stm32-rproc m4@0: wdg irq registered
[    2.092229] mmc0: new high speed SDHC card at address aaaa
[    2.095481] remoteproc remoteproc0: m4 is available
[    2.100845] mmc1: queuing unknown CIS tuple 0x80 (2 bytes)
[    2.106424] vref: supplied by vdd
[    2.112993] mmcblk0: mmc0:aaaa SS16G 14.8 GiB
[    2.114713] stm32-adc-core 48003000.adc: Linked as a consumer to regulator.4
[    2.120263] mmc1: queuing unknown CIS tuple 0x80 (3 bytes)
[    2.126247] stm32-adc-core 48003000.adc: Linked as a consumer to regulator.7
[    2.140582] mmc1: queuing unknown CIS tuple 0x80 (3 bytes)
[    2.147660] mmc1: queuing unknown CIS tuple 0x80 (7 bytes)
[    2.153675] mmc1: queuing unknown CIS tuple 0x80 (3 bytes)
[    2.161027] mmc1: queuing unknown CIS tuple 0x80 (6 bytes)
[    2.166021]  mmcblk0: p1 p2 p3 p4 p5 p6 p7
[    2.170019] iio iio:device2: Can't get offset/scale: -517
[    2.178126] optee: probing for conduit method from DT.
[    2.181819] optee: api uid mismatch
[    2.194802] NET: Registered protocol family 17
[    2.197882] can: controller area network core (rev 20170425 abi 9)
[    2.204107] NET: Registered protocol family 29
[    2.208562] can: raw protocol (rev 20170425)
[    2.212711] can: broadcast manager protocol (rev 20170425 t)
[    2.218430] can: netlink gateway (rev 20170425) max_hops=1
[    2.224447] Key type dns_resolver registered
[    2.228395] ThumbEE CPU extension supported.
[    2.232437] Registering SWP/SWPB emulation handler
[    2.238350] registered taskstats version 1
[    2.241321] Loading compiled-in X.509 certificates
[    2.256561] mmc1: new high speed SDIO card at address 0001
[    2.271548] stm32-usbphyc 5a006000.usbphyc: Linked as a consumer to regulator.1
[    2.277648] stm32-usbphyc 5a006000.usbphyc: Linked as a consumer to regulator.2
[    2.284843] stm32-usbphyc 5a006000.usbphyc: Linked as a consumer to regulator.12
[    2.292952] stm32-usbphyc 5a006000.usbphyc: registered rev:1.0
[    2.300080] dwc2 49000000.usb-otg: 49000000.usb-otg supply vusb_d not found, using dummy regulator
[    2.307842] dwc2 49000000.usb-otg: Linked as a consumer to regulator.0
[    2.314172] dwc2 49000000.usb-otg: 49000000.usb-otg supply vusb_a not found, using dummy regulator
[    2.335711] dwc2 49000000.usb-otg: EPs: 9, dedicated fifos, 952 entries in SPRAM
[    2.343383] ehci-platform 5800d000.usbh-ehci: EHCI Host Controller
[    2.348239] ehci-platform 5800d000.usbh-ehci: new USB bus registered, assigned bus number 1
[    2.356918] ehci-platform 5800d000.usbh-ehci: irq 63, io mem 0x5800d000
[    2.385833] ehci-platform 5800d000.usbh-ehci: USB 2.0 started, EHCI 1.00
[    2.392426] hub 1-0:1.0: USB hub found
[    2.394895] hub 1-0:1.0: 2 ports detected
[    2.401941] sii902x 0-0039: Linked as a consumer to regulator.10
[    2.406678] sii902x 0-0039: Linked as a consumer to regulator.14
[    2.416755] i2c i2c-0: Added multiplexed i2c bus 2
[    2.422661] cs42l51 0-004a: Linked as a consumer to regulator.8
[    2.427301] cs42l51 0-004a: Linked as a consumer to regulator.9
[    2.435839] cs42l51 0-004a: Cirrus Logic CS42L51, Revision: 01
[    2.443930] asoc-audio-graph-card sound: cs42l51-hifi0 <-> 4400b004.audio-controller mapping ok
[    2.452269] asoc-audio-graph-card sound: cs42l51-hifi1 <-> 4400b024.audio-controller mapping ok
[    2.460255] asoc-audio-graph-card sound: i2s-hifi <-> 4000b000.audio-controller mapping ok
[    2.469479] cs42l51 0-004a: ASoC: mux DAC Mux has no paths
[    2.709125] [drm] ltdc hw version 0x00010300 - ready
[    2.712732] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.719338] [drm] Driver supports precise vblank timestamp query.
[    2.726356] [drm] Initialized stm 1.0.0 20170330 for 5a001000.display-controller on minor 0
[    2.734870] stm32_rtc 5c004000.rtc: setting system clock to 2000-01-01 00:00:11 UTC (946684811)
[    2.743535] vdda: disabling
[    2.745686] ALSA device list:
[    2.748367]   #0: STM32M▒[    2.765870] usb 1-1: new high-speed USB device number 2 using ehci-platform
[    2.856532] EXT4-fs (mmcblk0p6): recovery complete
[    2.861617] EXT4-fs (mmcblk0p6): mounted filesystem with ordered data mode. Opts: (null)
[    2.868387] VFS: Mounted root (ext4 filesystem) on device 179:6.
[    2.881556] devtmpfs: mounted
[    2.884919] Freeing unused kernel memory: 1024K
[    2.888392] Run /sbin/init as init process
[    2.967532] hub 1-1:1.0: USB hub found
[    2.970090] hub 1-1:1.0: 4 ports detected
[    3.150593] systemd[1]: System time before build time, advancing clock.
[    3.251973] NET: Registered protocol family 10
[    3.295616] Segment Routing with IPv6
[    3.320321] systemd[1]: systemd 239 running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR +SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.341082] systemd[1]: Detected architecture arm.

Welcome to ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 2.6-openstlinux-19-02-20-github-display-fix (thud)!

[    3.400065] systemd[1]: Set hostname to <stm32mp1>.
[    3.412793] systemd[1]: Hardware watchdog 'STM32 Independent Watchdog', version 0
[    3.419989] systemd[1]: Set hardware watchdog to 30s.
[    4.069069] systemd[1]: Unnecessary job for dev-ttySTM0.device was removed.
[    4.076875] random: systemd: uninitialized urandom read (16 bytes read)
[    4.086986] systemd[1]: Created slice system-getty.slice.
[  OK  ] Created slice system-getty.slice.
[    4.126217] random: systemd: uninitialized urandom read (16 bytes read)
[    4.159036] systemd[1]: Listening on Process Core Dump Socket.
[  OK  ] Listening on Process Core Dump Socket.
[    4.196865] random: systemd: uninitialized urandom read (16 bytes read)
[    4.204111] systemd[1]: Created slice system-serial\x2dgetty.slice.
[  OK  ] Created slice system-serial\x2dgetty.slice.
[    4.237406] systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
[  OK  ] Listening on initctl Compatibility Named Pipe.
[  OK  ] Listening on Journal Socket (/dev/log).
[  OK  ] Listening on udev Kernel Socket.
[  OK  ] Listening on Syslog Socket.
[  OK  ] Reached target Remote File Systems.
[  OK  ] Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Reached target Swap.
[  OK  ] Listening on Network Service Netlink Socket.
[  OK  ] Created slice User and Session Slice.
[  OK  ] Listening on Journal Socket.
         Starting Create list of required st…ce nodes for the current kernel...
         Starting udev Coldplug all Devices...
         Mounting POSIX Message Queue File System...
         Starting Mount partitions...
         Starting Load Kernel Modules...
[  OK  ] Started Hardware RNG Entropy Gatherer Daemon.
[    4.756295] random: crng init done
[    4.758268] random: 7 urandom warning(s) missed due to ratelimiting
         Mounting Temporary Directory (/tmp)...
[  OK  ] Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Reached target Paths.
         Starting Remount Root and Kernel File Systems...
         Mounting Kernel Debug File System...
[  OK  ] Reached target Slices.
[    4.993262] EXT4-fs (mmcblk0p6): re-mounted. Opts: (null)
         Starting Journal Service...
[  OK  ] Started Create list of required sta…vice nodes for the current kernel.
[  OK  ] Mounted POSIX Message Queue File System.
[  OK  ] Started Load Kernel Modules.
[  OK  ] Mounted Temporary Directory (/tmp).
[  OK  ] Started Remount Root and Kernel File Systems.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Started Starts Psplash Boot screen.
[    5.240941] EXT4-fs (mmcblk0p4): recovery complete
[    5.248782] EXT4-fs (mmcblk0p4): mounted filesystem with ordered data mode. Opts: (null)
         Mounting Kernel Configuration File System...
         Starting Apply Kernel Variables...
         Mounting FUSE Control File System...
         Starting Create Static Device Nodes in /dev...
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Started Apply Kernel Variables.
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Started Create Static Device Nodes in /dev.
         Starting udev Kernel Device Manager...
[  OK  ] Reached target Local File Systems (Pre).
[  OK  ] Reached target Containers.
         Mounting /var/volatile...
[  OK  ] Mounted /var/volatile.
         Starting Load/Save Random Seed...
[  OK  ] Started Journal Service.
         Starting Flush Journal to Persistent Storage...
[  OK  ] Started Load/Save Random Seed.
[  OK  ] Started udev Kernel Device Manager.
[    6.024107] systemd-journald[153]: Received request to flush runtime journal from PID 1
[  OK  ] Started Flush Journal to Persistent Storage.
[    6.160816] EXT4-fs (mmcblk0p7): recovery complete
[    6.169210] EXT4-fs (mmcblk0p7): mounted filesystem with ordered data mode. Opts: (null)
[    6.649329] EXT4-fs (mmcblk0p5): recovery complete
[    6.655528] EXT4-fs (mmcblk0p5): mounted filesystem with ordered data mode. Opts: (null)
[  OK  ] Started Mount partitions.
[  OK  ] Reached target Local File Systems.
         Starting Create Volatile Files and Directories...
[  OK  ] Started Create Volatile Files and Directories.
         Starting Network Time Synchronization...
         Starting Update UTMP about System Boot/Shutdown...
[  OK  ] Started Update UTMP about System Boot/Shutdown.
[    7.331584] input: generic ft5x06 (11) as /devices/platform/soc/40012000.i2c/i2c-0/0-0038/input/input2
[  OK  ] Started udev Coldplug all Devices.
[    7.487274] Bluetooth: Core ver 2.22
[    7.499899] NET: Registered protocol family 31
[    7.531134] Bluetooth: HCI device and connection manager initialized
[    7.555188] Bluetooth: HCI socket layer initialized
[    7.559496] Bluetooth: L2CAP socket layer initialized
[    7.576992] Bluetooth: SCO socket layer initialized
[    7.633136] Bluetooth: HCI UART driver ver 2.3
[    7.636291] Bluetooth: HCI UART protocol H4 registered
[    7.661696] hci_uart_bcm serial0-0: No reset resource, using default baud rate
[    7.678187] Bluetooth: HCI UART protocol Broadcom registered
[    7.683541] galcore: loading out-of-tree module taints kernel.
[    7.779922] Galcore version 6.2.4.174315
[    7.957067] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    8.121439] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    8.246699] brcmfmac: brcmf_fw_alloc_request: using brcm/brcmfmac43430-sdio for chip BCM43430/1
[    8.496770] brcmfmac: brcmf_fw_alloc_request: using brcm/brcmfmac43430-sdio for chip BCM43430/1
[  OK  ] Started Network Time Synchronization.
[    8.586763] brcmfmac: brcmf_c_preinit_dcmds: Firmware: BCM43430/1 wl0: Sep 11 2018 09:22:09 version 7.45.98.65 (r707797 CY) FWID 01-b54727f
[    9.835901] Bluetooth: hci0: command 0xfc18 tx timeout
[  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Created slice system-systemd\x2dbacklight.slice.
         Starting Load/Save Screen Backlight…ess of backlight:5a000000.dsi.0...
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Load/Save Screen Backlight …tness of backlight:5a000000.dsi.0.
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Reached target System Initialization.
[  OK  ] Listening on dropbear.socket.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Listening on RPCbind Server Activation Socket.
         Starting Console System Startup Logging...
[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Basic System.
         Starting Enable USB Ethernet gadget...
[  OK  ] Started Kernel Logging Service.
         Starting Weston Wayland Compositor...
         Starting Save/Restore Sound Card State...
[  OK  ] Started ST Verify if eth0 network interface are already configured.
         Starting Network Service...
[   16.479780] using random self ethernet address
[   16.482786] using random host ethernet address
         Starting Netdata, Real-time performance monitoring...
         Starting Bluetooth service...
         Starting Login Service...
[  OK  ] Started D-Bus System Message Bus.
[   16.702439] usb0: HOST MAC 3a:d2:6c:14:e2:f6
[   16.705577] usb0: MAC e6:c8:9f:27:d7:0c
[   16.711562] dwc2 49000000.usb-otg: bound driver configfs-gadget
         Starting Sound Service...
[  OK  ] Started System Logging Service.
[  OK  ] Started TEE Supplicant.
[  OK  ] Started Network Service.
[   17.028077] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[  OK  ] Started Console System Startup Logging.
[   17.061523] Generic PHY stmmac-0:00: attached PHY driver [Generic PHY] (mii_bus:phy_addr=stmmac-0:00, irq=POLL)
[   17.103268] dwmac4: Master AXI performs any burst length
[  OK  ] Started S[   17.121398] stm32-dwmac 5800a000.ethernet eth0: No Safety Features support found
ave/Restore Sound [   17.130327] stm32-dwmac 5800a000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
Card State.
[   17.144865] stm32-dwmac 5800a000.ethernet eth0: registered PTP clock
[   17.151257] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
[  OK  ] Started Enable USB Ethernet gadget.
         Stopping Network Service...
[  OK  ] Reached target Sound Card.
[  OK  ] Stopped Network Service.
         Starting Network Service...
[   17.589716] Gcnano is present and activated
         Starting Hostname Service...
[  OK  ] Started Login Service.
[  OK  ] Started Bluetooth service.
[   17.757325] Bluetooth: hci0: BCM: failed to write update baudrate (-110)
[   17.762594] Bluetooth: hci0: Failed to set baudrate
[  OK  ] Reached target Bluetooth.
[  OK  ] Started Network Service.
         Starting Wait for Network to be Configured...
         Starting Network Name Resolution...
[  OK  ] Started Weston Wayland Compositor.
[  OK  ] Started Netdata, Real-time performance monitoring.
[  OK  ] Started Hostname Service.
[  OK  ] Started Sound Service.
[  OK  ] Started Network Name Resolution.
[  OK  ] Reached target Network.
[  OK  ] Started IIO Daemon.
         Starting Target Communication Framework agent...
         Starting Permit User Sessions...
         Starting Avahi mDNS/DNS-SD Stack...
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started Permit User Sessions.
[  OK  ] Started Getty on tty1.
[  OK  ] Started Serial Getty on ttySTM0.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started Target Communication Framework agent.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Reached target Multi-User System.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Started Update UTMP about System Runlevel Changes.
[   19.835925] Bluetooth: hci0: command 0x0c03 tx timeout

ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 2.6-openstlinux-19-02-20-github-display-fix stm32mp1 ttySTM0

stm32mp1 login: root (automatic login)

```