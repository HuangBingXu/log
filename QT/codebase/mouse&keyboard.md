### mouse

* event

```C++
    void mousePressEvent(QMouseEvent *event);        //单击
    void mouseReleaseEvent(QMouseEvent *event);      //释放
    void mouseDoubleClickEvent(QMouseEvent *event);  //双击
    void mouseMoveEvent(QMouseEvent *event);         //移动
    void wheelEvent(QWheelEvent *event);             //滑轮
```



* use:

> ```c++
> #include <QMouseEvent>
> ```



```
void Widget::mousePressEvent(QMouseEvent *event)
{
    // 如果是鼠标左键按下   改变指针形状，并且存储当前指针位置与窗口位置的差值。
    if(event->button() == Qt::LeftButton){
    }
    // 如果是鼠标右键按下
    else if(event->button() == Qt::RightButton){
    }
}
```



* add in **.h**

```
protected:
    void mousePressEvent(QMouseEvent *event);
```



#### keyboard

* event

  ```
      void keyPressEvent(QKeyEvent *event);
  
      void keyReleaseEvent(QKeyEvent *event);
  ```

  

* use

  ```
  void Widget::keyPressEvent(QKeyEvent *event)
  {
  
      if(event->key() == Qt::Key_Up){
          // 按键重复时不做处理
          if(event->isAutoRepeat()) return;
          // 标记向上方向键已经按下
          keyUp = true;
  
      }else if(event->key() == Qt::Key_Left){
          if(event->isAutoRepeat()) return;
          keyLeft = true;
      }
  }
  ```

  

* release

  ```
  // 按键释放事件
  void Widget::keyReleaseEvent(QKeyEvent *event)
  {
      //如果是处理两个普通按键，得避免自动重复
     if(event->key() == Qt::Key_Up){
          if(event->isAutoRepeat()) return;
      }
  
      else if(event->key() == Qt::Key_Left){
          if(event->isAutoRepeat()) return;
     }
  }
  
  ```

* add in **.h**

  ```
  protected:
      void keyPressEvent(QKeyEvent *event);
      void keyReleaseEvent(QKeyEvent *event)
  ```

  

