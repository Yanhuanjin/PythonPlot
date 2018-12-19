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
                plt.plot([i*(1+boundary_adjust),(i+1)*(1-boundary_adjust)],[group[j], group[j]], color, linewidth=2.8)
                i = i + 2
                j = j + 1

plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])

# points input 
points_1 = [0.0, 0.6, 0.2, 0.0, 0.2]
points_2 = [0.0, 0.5,-0.3, 0.2]
points_3 = [0.0, 0.4,-0.2, 0.1]

# preconditioning
group_1 = plot_line(points_1)
group_2 = plot_line(points_2)
group_3 = plot_line(points_3)

# points plot
plt.plot(group_1, ':r',label="a")
plt.plot(group_2, '-g',label="b")
plt.plot(group_3, '-.b',label="c")
pl.legend()

# plot bar
horizon_line(points_1, 'r')
horizon_line(points_2, 'g')
horizon_line(points_3, 'b')

plt.show()   
