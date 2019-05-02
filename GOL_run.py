import numpy as np
import sys
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from collections import Counter
from GOL_class import GOL
from datetime import date



###############################################################
#User instructions:
# to run code in the terminal:
# python GOL_run.py <Lattice Size> <Initial Conditions> <task>

#Intial Conditions are : blinker, glider, absorbing, random
#tasks are: viz or data
###############################################################


#Create an instance of GOL
A = GOL(int(sys.argv[1]),str(sys.argv[2]))


#Animates the simulation of GOL if user selects
if (sys.argv[3])=='viz':


    #Update plot function which sweeps the array and simulates the GOL
    def UpdatePlot(*args):
        image.set_array(A.array)
        A.Sweep()
        return image,

    #Animating the simulation. plt.imshow creates much faster moving animations so it is used here.
    GLImage = plt.figure()
    image = plt.imshow(A.array,animated=True)
    model = FuncAnimation(GLImage,UpdatePlot,interval=50,blit=True)
    plt.show()

#If user selects, simulates GOL for selected number of sweeps and calculates the velocity of the glider. NOTE: only works if initial condition is "glider"
elif (sys.argv[3])=='data':

    time = 0
    print(A.array)
    
    #required to make it work
    sweeps=140
    for i in range(sweeps):
        A.Sweep()
        time_list,CoM_list,time=A.Get_CoM(time)

    print('Velocity of the Glider is: %.3f'%(A.Get_Velocity(time_list,CoM_list)))
    plt.plot(time_list,CoM_list)
    plt.ylabel('CoM position')
    plt.xlabel('Time')
    plt.title('Centre of Mass Position vs Time')
    plt.savefig('Velocity_plot_50x50_'+str(date.today()),format='pdf')
    
    plt.show()


