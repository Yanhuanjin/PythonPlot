import matplotlib.pyplot as plt

"""Expert version"""

def plot_line(float_points):
        final_points = []
        for point in float_points:
                for i in range(2):
                        final_points.append(point)
        return(final_points)


plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])

# points input and preconditioning
points_1 = [0,0.6,0.2,0]
points_2 = [0,0.5,-0.3,0.2]
points_3 = [0,0.4,-0.2,0.1]

group_1 = plot_line(points_1)
group_2 = plot_line(points_2)
group_3 = plot_line(points_3)

# points plot
plt.plot(group_1, ':r',label="a")
plt.plot(group_2, '-g',label="b")
plt.plot(group_3, '-.b',label="c")
plt.show()   
