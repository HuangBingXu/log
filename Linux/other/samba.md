文件共享：
Samba:
ubuntu 设置samba server:                    
https://www.cnblogs.com/phinecos/archive/2009/06/06/1497717.html

* 安装

  ```
  sudo apt-get install samba
  sudo apt-get install cifs-utils
  ```

* 修改配置文件

* 

  * 备份现有配置

    > sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak

  * 修改配置：

    > sudo vi /etc/samba/smb.conf

    ```
    [share]
          path = /home/halin/share
          available = yes
          browsealbe = yes
          public = yes
          writable = yes
    ```

* 创建samba帐户

  ```
   sudo touch /etc/samba/smbpasswd
   sudo smbpasswd -a halin
  ```

* 重启samba服务器

  > sudo /etc/init.d/samba restart

