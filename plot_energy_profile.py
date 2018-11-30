import matplotlib.pyplot as plt

values = []   # 输入数据列表
points = []   # 处理数据列表
n = 1
while True:
    print('Please input Point-%d:' %(n))
    point = input()
    n = n + 1
    if point == '':
        print("INPUT OVER.\n")
        break
    else:
        values.append(float(point))

for value in values:
    for i in range(2):              # 增加一组平行的数据点集合，绘制横线段而不是单纯描点
        points.append(value)    

plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])
plt.plot(range(len(points)), points, '-')
plt.show()   
