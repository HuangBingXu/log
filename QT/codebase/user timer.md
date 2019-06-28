头文件中
> #include "QTimer"

声明：
```
public slots:
    void Timeout_handler();

```

CPP中：
```
    QTimer *timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(Timeout_handler()));
    timer->start(1000);

void Dialog::Timeout_handler()
{

}
```