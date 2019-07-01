#### lsb_relase
Printing distribution specific information

```
Board $> lsb_release -a
LSB Version:    core-5.0-noarch:core-5.0-arm
Distributor ID: openstlinux-weston
Description:    ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 2.6-openstlinux-4.19-thud-mp1-19-02-20
Release:        2.6-openstlinux-4.19-thud-mp1-19-02-20
Codename:       thud
```

#### uname 
Printing system information

```
Board $> uname -a
Linux stm32mp1 4.19.9 #1 SMP PREEMPT Thu Dec 13 08:16:23 UTC 2018 armv7l armv7l armv7l GNU/Linux
```

#### Printing Linux kernel and GCC versions
```
Board $> cat /proc/version
Linux version 4.19.9 (oe-user@oe-host) (gcc version 8.2.0 (GCC)) #1 SMP PREEMPT Thu Dec 13 08:16:23 UTC 2018
```

#### 查看系统发布信息：cat /etc/os-release
```
NAME="Ubuntu"
VERSION="16.04.5 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.5 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```