import matplotlib.pyplot as plt

values = []
points = []
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
    for i in range(2):
        points.append(value)

plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])
plt.plot(range(len(points)), points, '-')
plt.show()   
