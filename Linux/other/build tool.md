把编译工具添加到环境变量

假如编译工具所在bin目录为**compile_path**

* 添加到临时变量

> export PATH=$PATH: compile_path

然后使用命令

> echo $PATH

查看有没有添加成功，使用该方法，只有在该终端中有效，

* 修改用户配置文件 

在文件“**~/.bashrc**”或者“**~/.bash_profile**” 中添加**export PATH=$PATH: compile_path**

使用该方法，只有相应的用户有效，

* 修改全局配置文件 

  在文件“**/etc/profile **” 中添加**export PATH=$PATH: compile_path**

  对该电脑中所有用户有效



