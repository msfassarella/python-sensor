#!/usr/bin/python
#coding: utf-8
#https://towardsdatascience.com/how-to-create-animated-graphs-in-python-bb619cc2dec1
#https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as img 
from matplotlib import animation
#from matplotlib.pylab import *      #not recommended
from mpl_toolkits.axes_grid1 import host_subplot


filepath = ""
filename = "SensorA_Log_N000.csv"

try:
   df = pd.read_csv(filepath + filename,",", header=0)

    #print(df.head(5))     # print the 5 first lines
    #print(df.tail(5))     # print the 5 last lines
    #print(df.__len__)     # print the file len
except:
    print("File not found")
    raise



timeinit = df.at[0,'T [ms]']

####### ANIMATION #########

# Setup figure and subplots
f0 = plt.figure(num = 0, figsize = (12, 8))#, dpi = 100)
f0.suptitle("Sensor", fontsize=12)
ax01 = plt.subplot2grid((2, 2), (0, 0))
ax02 = plt.subplot2grid((2, 2), (0, 1))
ax03 = plt.subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
ax04 = ax03.twinx()
#tight_layout()

# Set titles of subplots
ax01.set_title('Magnetometer')
ax02.set_title('Giroscope')
ax03.set_title('Accelerometer')

# set y-limits
ax01.set_ylim(-7,7)
ax02.set_ylim(-9,9)
ax03.set_ylim(-2,2)
ax04.set_ylim(-2,2)

# sex x-limits
ax01.set_xlim(0,1000)
ax02.set_xlim(0,1000)
ax03.set_xlim(0,1000)
ax04.set_xlim(0,1000)


# First set up the figure, the axis, and the plot element we want to animate
#fig = plt.figure()
#ax = plt.axes(xlim=(0, 1000), ylim=(-6, 6))
line11, = ax01.plot([], [], 'r-', lw=2, label = "MagX")
line12, = ax01.plot([], [],'g-', lw=2, label="MagY")
line13, = ax01.plot([], [],'b-', lw=2, label="MagZ")

line21, = ax02.plot([], [], 'r-', lw=2, label = "GiroX")
line22, = ax02.plot([], [],'g-', lw=2, label="GiroY")
line23, = ax02.plot([], [],'b-', lw=2, label="GiroZ")

line31, = ax03.plot([], [], 'r-', lw=2, label = "AccelX")
line32, = ax03.plot([], [],'g-', lw=2, label="AccelY")
line33, = ax03.plot([], [],'b-', lw=2, label="AccelZ")


# set label names
ax01.set_xlabel("t")
ax01.set_ylabel("mgauss")
ax02.set_xlabel("t")
ax02.set_ylabel("mdps")
ax03.set_xlabel("t")
ax03.set_ylabel("mg")



def init():
    line11.set_data([], [])
    line12.set_data([], [])
    line13.set_data([], [])
    
    line21.set_data([], [])
    line22.set_data([], [])
    line23.set_data([], [])

    line31.set_data([], [])
    line32.set_data([], [])
    line33.set_data([], [])
    return line11, line12, line13, line21, line22, line23, line31, line32, line33,

def animates(i):
    global df

    passo = 1
    posstart = i * passo
    posstop = 20 + i * passo
    dfplot = df[posstart:posstop]
    x = dfplot['T [ms]'].to_numpy() - dfplot.at[posstart,'T [ms]']
    
    y11 = dfplot['MagX [mgauss]'].to_numpy() / 1000
    y12 = dfplot['MagY [mgauss]'].to_numpy() / 1000
    y13 = dfplot['MagZ [mgauss]'].to_numpy() / 1000

    y21 = dfplot['GyroX [mdps]'].to_numpy() / 5500
    y22 = dfplot['GyroY [mdps]'].to_numpy() / 5500
    y23 = dfplot['GyroZ [mdps]'].to_numpy() / 5500

    y31 = dfplot['AccX [mg]'].to_numpy() / 1000
    y32 = dfplot['AccY [mg]'].to_numpy() / 1000
    y33 = dfplot['AccZ [mg]'].to_numpy() / 1000

   
    line11.set_data(x,y11)
    line12.set_data(x,y12)
    line13.set_data(x,y13)

    line21.set_data(x,y21)
    line22.set_data(x,y22)
    line23.set_data(x,y23)

    line31.set_data(x,y31)
    line32.set_data(x,y32)
    line33.set_data(x,y33)

    return line11, line12, line13, line21, line22, line23, line31, line32, line33,

#resultado = animates(1)
#print(resultado)

anim = animation.FuncAnimation(f0, animates, init_func=init, frames=1500, interval=30, blit=True)
anim.save('basic_animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
plt.show()



