
Qt Charts是基于Qt Graphics View实现的一个图表的组件，可以用来创建现在风格的、可交互的、以数据为中心的图表，可以用作QWidget或者 QGraphicsWidget，也可用在QML中.

QT提供的相关的class有：

![](img/cpp_class.png)

主要有：
* [QChartView Class](https://doc.qt.io/qt-5/qchartview.html)
一个用来显示图表的widget，
```
QChartView <-- QGraphicsView <-- QAbstractScrollArea <-- QFrame <-- QWidget
```

* [QChart](https://doc.qt.io/qt-5/qchart.html)
  QChart是QGraphicsWidget，可以在QGraphicsScene上显示，管理图表中的数据、图例、坐标轴等，
  ```
  QChart <-- QGraphicsWidget <-- QGraphicsObject and QGraphicsLayoutItem
  QGraphicsObject  <--  QObject and QGraphicsItem
  ```
*  图表类型
    * [ QLineSeries]()
    * [QSplineSeries ]()
    * [QAreaSeries ]()
    * [QScatterSeries ]()
    * [QAbstractBarSeries]()
    * [QPieSeries ]()
    * [QBoxPlotSeries ]()
    * [ QCandlestickSeries]()
* [QAbstractAxis ]():坐标轴
* 图例:
  基类为[QLegendMarker](),




