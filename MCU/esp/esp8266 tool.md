安装一些依赖：

```
apt-get install git autoconf build-essential gperf bison flex texinfo libtool libncurses5-dev wget gawk python-serial libexpat-dev
```





下载源码：

> ```
> git clone -b lx106 git://github.com/jcmvbkbc/crosstool-NG.git 
> ```



然后：

```
cd crosstool-NG
./bootstrap && ./configure --prefix=`pwd` && make && make install
./ct-ng xtensa-lx106-elf
./ct-ng build
```





* 出现了如下错误：

  ```
  [ALL  ]    --2019-08-06 15:44:32--  http://mirrors.kernel.org/sources.redhat.com/newlib/newlib-2.0.0
  [ALL  ]    Resolving mirrors.kernel.org (mirrors.kernel.org)... 149.20.37.36, 2001:4f8:4:6f:0:1994:3:14
  [ALL  ]    Connecting to mirrors.kernel.org (mirrors.kernel.org)|149.20.37.36|:80... connected.
  [ALL  ]    HTTP request sent, awaiting response... Read error (Connection reset by peer) in headers.
  [ALL  ]    Retrying.
  [ALL  ]    
  [ALL  ]    --2019-08-06 15:44:33--  (try: 2)  http://mirrors.kernel.org/sources.redhat.com/newlib/newlib-2.0.0
  [ALL  ]    Connecting to mirrors.kernel.org (mirrors.kernel.org)|149.20.37.36|:80... connected.
  [ALL  ]    HTTP request sent, awaiting response... Read error (Connection reset by peer) in headers.
  [ALL  ]    Retrying.
  [ALL  ]    
  [ALL  ]    --2019-08-06 15:44:35--  (try: 3)  http://mirrors.kernel.org/sources.redhat.com/newlib/newlib-2.0.0
  [ALL  ]    Connecting to mirrors.kernel.org (mirrors.kernel.org)|149.20.37.36|:80... connected.
  [ALL  ]    HTTP request sent, awaiting response... Read error (Connection reset by peer) in headers.
  [ALL  ]    Giving up.
  [ALL  ]    
  [DEBUG]    Not at this location: "http://mirrors.kernel.org/sources.redhat.com/newlib/newlib-2.0.0"
  [ERROR]  
  [ERROR]  >>
  [ERROR]  >>  Build failed in step 'Retrieving needed toolchain components' tarballs'
  [ERROR]  >>        called in step '(top-level)'
  [ERROR]  >>
  [ERROR]  >>  Error happened in: do_libc_get[scripts/build/libc/newlib.sh@741]
  [ERROR]  >>        called from: main[scripts/crosstool-NG.sh@594]
  [ERROR]  >>
  [ERROR]  >>  For more info on this error, look at the file: 'build.log'
  [ERROR]  >>  There is a list of known issues, some with workarounds, in:
  [ERROR]  >>      'share/doc/crosstool-ng/crosstool-ng-1.22.0-66-ga4286b8/B - Known issues.txt'
  [ERROR]  
  [ERROR]  (elapsed: 0:54.40)
  ```

  解决办法：

  从网上下载**newlib-2.0.0**，然后放到文件夹**/*/crosstool-NG/.build/tarballs**中



* python is missing or unusable

  ```
  [INFO ]  Installing cross-gdb
  [ERROR]    configure: error: python is missing or unusable
  [ERROR]    make[2]: *** [configure-gdb] Error 1
  [ERROR]    make[1]: *** [all] Error 2
  [ERROR]
  [ERROR]  >>
  [ERROR]  >>  Build failed in step 'Installing cross-gdb'
  [ERROR]  >>        called in step '(top-level)'
  [ERROR]  >>
  [ERROR]  >>  Error happened in: CT_DoExecLog[scripts/functions@257]
  [ERROR]  >>        called from: do_debug_gdb_build[scripts/build/debug/300-gdb.sh@120]
  [ERROR]  >>        called from: do_debug[scripts/build/debug.sh@35]
  [ERROR]  >>        called from: main[scripts/crosstool-NG.sh@646]
  [ERROR]  >>
  [ERROR]  >>  For more info on this error, look at the file: 'build.log'
  [ERROR]  >>  There is a list of known issues, some with workarounds, in:
  [ERROR]  >>      'share/doc/crosstool-ng/crosstool-ng-1.22.0-66-ga4286b8-dirty/B - Known issues.txt'
  [ERROR]
  [ERROR]  (elapsed: 14:40.92)
  [14:41] / ct-ng:152: recipe for target 'build' failed
  make: *** [build] Error 2
  ```

  一开始是以为没安装Python或者找不到python，又重新安装了python还是不行，后来想到可能是没有相关库，于是安装了python相关库：

  > sudo apt-get install python-dev

  就可以成功编译了，编译完完整log如下：

  ```shell
  hl@hl-ub:~/share/ESP/8266/crosstool-NG$ ./ct-ng build
  [INFO ]  Performing some trivial sanity checks
  [INFO ]  Build started 20190807.091005
  [INFO ]  Building environment variables
  [INFO ]  =================================================================
  [INFO ]  Retrieving needed toolchain components' tarballs
  [INFO ]  Retrieving needed toolchain components' tarballs: done in 0.06s (at 00:07)
  [INFO ]  =================================================================
  [INFO ]  Extracting and patching toolchain components
  [INFO ]  Extracting and patching toolchain components: done in 0.41s (at 00:07)
  [INFO ]  =================================================================
  [INFO ]  Installing ncurses for build
  [INFO ]  Installing ncurses for build: done in 35.64s (at 00:43)
  [INFO ]  =================================================================
  [INFO ]  Installing GMP for host
  [INFO ]  Installing GMP for host: done in 41.21s (at 01:24)
  [INFO ]  =================================================================
  [INFO ]  Installing MPFR for host
  [INFO ]  Installing MPFR for host: done in 31.29s (at 01:56)
  [INFO ]  =================================================================
  [INFO ]  Installing ISL for host
  [INFO ]  Installing ISL for host: done in 30.30s (at 02:26)
  [INFO ]  =================================================================
  [INFO ]  Installing CLooG for host
  [INFO ]  Installing CLooG for host: done in 6.42s (at 02:32)
  [INFO ]  =================================================================
  [INFO ]  Installing MPC for host
  [INFO ]  Installing MPC for host: done in 14.16s (at 02:46)
  [INFO ]  =================================================================
  [INFO ]  Installing expat for host
  [INFO ]  Installing expat for host: done in 5.75s (at 02:52)
  [INFO ]  =================================================================
  [INFO ]  Installing binutils for host
  [INFO ]  Installing binutils for host: done in 67.08s (at 03:59)
  [INFO ]  =================================================================
  [INFO ]  Installing C library headers & start files
  [INFO ]  Installing C library headers & start files: done in 0.14s (at 03:59)
  [INFO ]  =================================================================
  [INFO ]  Installing pass-2 core C gcc compiler
  [INFO ]  Installing pass-2 core C gcc compiler: done in 256.59s (at 08:16)
  [INFO ]  =================================================================
  [INFO ]  Installing C library
  [INFO ]  Installing C library: done in 40.74s (at 08:57)
  [INFO ]  =================================================================
  [INFO ]  Installing final gcc compiler
  [INFO ]  Installing final gcc compiler: done in 303.89s (at 14:01)
  [INFO ]  =================================================================
  [INFO ]  Installing cross-gdb
  [INFO ]  Installing cross-gdb: done in 147.77s (at 16:29)
  [INFO ]  =================================================================
  [INFO ]  Cleaning-up the toolchain's directory
  [INFO ]    Stripping all toolchain executables
  [INFO ]  Cleaning-up the toolchain's directory: done in 2.39s (at 16:31)
  [INFO ]  Build completed at 20190807.092635
  [INFO ]  (elapsed: 16:29.99)
  [INFO ]  Finishing installation (may take a few seconds)...
  ```

  



由于之前配置的时候，使用了**--prefix=`pwd`**选项，所以编译出来的工具在***/crosstool-NG/builds/xtensa-lx106-elf**，把该路径添加到环境变量就可以使用了