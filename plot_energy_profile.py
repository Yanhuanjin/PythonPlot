import matplotlib.pyplot as plt

"""Lazy version"""

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

def plot_line(float_points):
        final_points = []
        for point in float_points:
                for i in range(2):
                        final_points.append(point)
        return(final_points)

line_group = []
all_points = []
line_number = int(input("******* Energy_ploter (Lazy mode) *******\nFor further use please edit the sorce code at\nhttps://github.com/Yanhuanjin/PythonPlot\n\nHow many lines do you want to draw?\n"))
for i in range(line_number):
        line_group.append(i)
        all_points.append(i)


plt.xlabel('Reaction Coordinate')
plt.ylabel('Energy')
plt.xticks([])
for i in line_group:
        print('>> group '+ str(i+1) + " \n")
        line_group[i] = plot_input()
        all_points[i] = plot_line(line_group[i])
        plt.plot(all_points[i], ':')
plt.show()   
