#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.005)
y = np.exp(-x/2.0)*np.sin(2*np.pi*x)

fig, ax  = plt.subplots()
ax.plot(x,y)
ax.set_xlim(0, 10)
ax.set_ylim(-1,1)

xdata, ydata= 5, 0
# xdisplay, ydisplay = ax.transData.transform_point(xdata,ydata)
xdisplay, ydisplay = ax.transData.transform_point((xdata, ydata))
print(xdisplay,ydisplay)

bbox = dict(boxstyle='round', fc='0.8')
arrowprops = dict(arrowstyle='->', connectionstyle='angle,angleA=0,angleB=90,rad=10')


offset = 72

ax.annotate('data=(%.1f,%.1f)'%(xdata,ydata),
            (xdata,ydata), xytext=(-2*offset,offset),textcoords='offset points',
            bbox=bbox,arrowprops=arrowprops
            )

disp = ax.annotate('display=(%.1f,%.1f)'%(xdisplay,ydisplay),xy=(xdata,ydata),
                   xytext=(0.5*offset,-offset), textcoords='offset points',bbox=bbox,
                   arrowprops=arrowprops
                   )
plt.show()