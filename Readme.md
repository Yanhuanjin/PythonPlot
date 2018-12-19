# 懒人版说明（LAZY VERSION） 

## 输入数据点

根据提示，输入需要描点的数据点，按回车表示结束，输入完毕再按一次回车。即可自动绘制势能面图。

# 专业版说明 (EXPERT VERSION)

## 输入坐标  points input
points_1 = [0.0, 0.5, -0.3, 0.015, -0.017]

## 预处理  preconditioning
group_1 = plot_line(points_1)

## 绘点  points plot
plt.plot(group_1, color = 'tab:blue', linestyle=':', label="a")

## 绘制水平线段 plot bar
horizon_line(points_1, 'tab:blue')

## 更改线条颜色和形状，标签
plt.plot(group_1, color='tab:blue', linestyle=':',  label="a")

color = ''  # 改颜色（支持RGB, 输入[色号](https://matplotlib.org/gallery/color/named_colors.html)即可)

linestyle = '' # 改线条（虚线'--' 点划线'-.' 点线':' 直线'-'）

label = ''	  # 改标签


## 更改坐标名称
横坐标更改`plt.xlabel()`括号里的内容

纵坐标更改`plt.ylabel()`括号里的内容

本说明列举了一些常用的功能，其他的都可以在Matplotlib文档中找到。

*# 详见[https://matplotlib.org/](https://matplotlib.org/ "Matplotlib")。*
