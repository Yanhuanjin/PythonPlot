# 
## 更改颜色
`plt.plot(range(len(points)), points)`

在这句代码后面增加一个输入，代表颜色即可

例如，`plt.plot(range(len(points)), points, 'r')`代表红色red，其他颜色也都可以用缩写代替。

## 更改线的形式
- 实线：'-'
- 虚线：'--'
- 点划线：'-.'
- 点线：':'
 
`plt.plot(range(len(points)), points, 'r--')`代表红色虚线


## 更改坐标名称
横坐标更改`plt.xlabel()`括号里的内容

纵坐标更改`plt.ylabel()`括号里的内容

本说明列举了一些常用的功能，其他的都可以在Matplotlib文档中找到。

*# 详见[https://matplotlib.org/](https://matplotlib.org/ "Matplotlib")。*