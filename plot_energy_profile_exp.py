import matplotlib.pyplot as plt
import pylab as pl

"""Expert version"""

def plot_line(float_points):
        final_points = []
        for point in float_points:
                for i in range(2):
                        final_points.append(point)
        return(final_points)

def horizon_line(group, color):
        i=0
        j=0
        boundary_adjust = 0.003
        while (i< len(group)*2):
                plt.plot([i*(1+boundary_adjust),(i+1)*(1-boundary_adjust)],[group[j], group[j]], color, linewidth=2.5)
                i = i + 2
                j = j + 1



plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])

# points input 
points_1 = [0.0, 0.5, -0.3, 0.015, -0.017]
#points_2 = [0.0, 0.5,-0.1, 0.2, 0.0]
points_3 = [0.0, 0.4,-0.2, 0.1, 0.014]
points_4 = [0.0, 0.3,-0.1, 0.21, -0.1]

# preconditioning
group_1 = plot_line(points_1)
#group_2 = plot_line(points_2)
group_3 = plot_line(points_3)
group_4 = plot_line(points_4)

# points plot
plt.plot(group_1, color = 'tab:blue', linestyle=':', label="a")
#plt.plot(group_2, color = 'tab:red', linestyle='-', label="b")
plt.plot(group_3, color = 'tab:green', linestyle='-.', label="c")
plt.plot(group_4, color = 'tab:orange', linestyle='--', label="d")
pl.legend()

# plot bar
horizon_line(points_1, 'tab:blue')
#horizon_line(points_2, 'tab:red')
horizon_line(points_3, 'tab:green')
horizon_line(points_4, 'tab:orange')

plt.show()   
