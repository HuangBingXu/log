文件**u-boot\lib\fdtdec.c**中：





文件**u-boot\lib\libfdt\fdt_ro.c**中；

* fdt_path_offset

> int fdt_path_offset(const void **fdt*, const char **path*)

获得dtb下某个节点的路径path的偏移。这个偏移就代表了这个节点。

* **fdt_getprop**

> const void *fdt_getprop(const void **fdt*, int *nodeoffset*, const char **name*, int **lenp*)

获得节点node的某个字符串属性值。