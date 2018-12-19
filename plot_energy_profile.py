import matplotlib.pyplot as plt
#import random


"""Lazy version"""

log = "******* Energy_ploter (Lazy mode) *******\n For further use or Expert version, please edit the sorce code.\n https://github.com/Yanhuanjin/PythonPlot "


def plot_input():
        plot_points = []
        float_points = []
        n = 1
        while True:
                print('Please input point %d:' %(n))
                point = input()
                n = n + 1
                if point == '':
                        print("INPUT OVER.\n")
                        break
                else:
                        float_points.append(float(point))
        return(float_points)


def horizon_points(float_points):
        final_points = []
        for point in float_points:
                for i in range(2):
                        final_points.append(point)
        return(final_points)


def horizon_line(group, color):
        i=0
        j=0

        while (i<= len(group)+1):
                try:
                        plt.plot([i,i+1],[group[j], group[j]], color, linewidth=3.0,)
                        i = i + 2
                        j = j + 1
                except IndexError:
                        print('Your input must accord with the number of line group!')
                        exit()

                        
def plot_line(points, color, style='-'):
        plt.plot(points, color, linestyle=style)


line_group = []
all_points = []

number_of_line = int(input(log + "\n\nHow many lines do you want to draw?\n"))

for i in range(number_of_line):
        line_group.append(i)
        all_points.append(i)

plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])
color_box =['red' ,'royalblue', 'g', 'k', 'orange', 'darkturquoise', 'b', 'm']
#random.shuffle(color_box)
for i in line_group:
        print('>> group '+ str(i+1) + " \n")
        line_group[i] = plot_input()
        all_points[i] = horizon_points(line_group[i])
        plot_line(all_points[i], color_box[i],style=':')
        horizon_line(line_group[i], color_box[i])
plt.show()   

