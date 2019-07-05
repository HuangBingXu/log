槽函数（次线程）中更新了UI,会引起如下错误：
```
ASSERT failure in QCoreApplication::sendEvent: “Cannot send events to objects owned by a different thread. Current thread e346e8. Receiver customWidget’ (of type ‘MainWindow’) was created in thread 4186a0”, file kernel\qcoreapplication.cpp, line 553
```
会出现这种情况是因为Qt做了限制（其它大多数GUI编程也一样），不允许在其它线程（非主线程）中访问UI控件，这么做主要是怕在多线程环境下对界面控件进行操作会出现不可预知的情况。


当关闭主界面的时候，很有可能次线程正在运行，这时，就会出现如下提示：
> QThread: Destroyed while thread is still running
这是因为次线程还在运行，就结束了UI主线程，导致事件循环结束。解决方法：
* 发起线程退出操作，调用quit()或exit()。
* 等待线程完全停止，删除创建在堆上的对象。
* 适当的使用wait()（用于等待线程的退出）和合理的算法。


QT GUI必须工作在主线程，所有部件和几个相关的类（？）不能工作在次线程

