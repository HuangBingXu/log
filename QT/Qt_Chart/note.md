1. 
A chart view does not require a QGraphicsScene object to work. To display a chart in an existing QGraphicsScene, the QChart or QPolarChart class should be used instead.

chart view不需要QGraphicsScene就可以工作，如果在现有的QGraphicsScene中显示chart,就可以不用QChart或者QPolarChart

2. 
A simpler solution is to display a chart in a layout by using the convenience class QChartView instead of QChart. 
在一个layout中显示图表的简单的方法是使用QChartView替换QChart？

3. 
Animation  Option  动画选项
```
AnimationOption { 
NoAnimation, 
GridAxisAnimations, 
SeriesAnimations, 
AllAnimations 
}
```

4. ChartTheme：
```
QChart::ChartThemeLight  				The light theme, which is the default theme.
QChart::ChartThemeBlueCerulean 			The cerulean blue theme.
QChart::ChartThemeDark 					The dark theme.
QChart::ChartThemeBrownSand 			The sand brown theme.
QChart::ChartThemeBlueNcs 				The natural color system (NCS) blue theme.
QChart::ChartThemeHighContrast 			The high contrast theme.
QChart::ChartThemeBlueIcy 				The icy blue theme.
QChart::ChartThemeQt 					The Qt theme.
```

5. ChartType：

QChart::ChartTypeUndefined		The chart type is not defined.            
QChart::ChartTypeCartesian		A cartesian chart.	笛卡尔坐标系            
QChart::ChartTypePolar			A polar chart.		极坐标细                


 6. The chart components can be used as QWidget or QGraphicsWidget objects
   一个图表（完整的图标，包括QChartView、QChart等），可以用作QWidget或者QGraphicsWidget



QChart is a QGraphicsWidget，一个绘图widget
Qt Charts uses the Graphics View Framework for ease of integration
The chart components can be used as QWidget or QGraphicsWidget objects or QML types.

The QGraphicsView class provides a widget for displaying the contents of a QGraphicsScene.
The QGraphicsScene class provides a surface for managing a large number of 2D graphical items.The class serves as a container for QGraphicsItems
Qt Charts can be used as QWidgets, QGraphicsWidget, or QML types.

Qt Graphics View Framework
Graphics View 提供了一种接口，用于管理大量自定义的 2D 图形元素，并与之进行交互；还提供了用于将这些元素进行可视化显示的观察组件，并支持缩放和旋转。
Graphics View 框架包含了一套完整的事件体系，可以用于与场景中的元素进行双精度的交互。这些元素同样支持键盘事件、鼠标事件等。Graphics View 使用了 
BSP 树（Binary Space Partitioning tree，这是一种被广泛应用于图形学方面的数据结构）来提供非常快速的元素发现，也正因为如此，
才能够实现一种上百万数量级元素的实时显示机制。
Graphics View 是一个基于元素（item）的 MV 架构的框架。它可以分成三个部分：元素 item、场景 scene 和视图 view。
Graphics View Framework 有三个主要部分：
    QGraphicsScene：能够管理元素的非 GUI 容器；
    QGraphicsItem：能够被添加到场景的元素；
    QGraphicsView：能够观察场景的可视化组件视图。












# 问题
The chart components can be used as QWidget or QGraphicsWidget objects    
chart components是指什么

A simpler solution is to display a chart in a layout by using the convenience class QChartView instead of QChart.
这句话什么意思？