#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
#
# plt.subplot(111)
# x1 = np.arange(0,6,0.025)
# y1 = np.sin(x1*np.pi/3)
# plt.plot(x1, y1, linewidth=4)
# plt.plot()
# x2 = np.arange(0,1.5,0.025)
#
# plt.show()

x = np.arange(0, 2*np.pi, 0.02)
y = np.sin(x)
y1 = np.sin(2*x)
y2 = np.sin(3*x)
ym1 = np.ma.masked_where(y1>0.5, y1)
ym2 = np.ma.masked_where(y2<-0.5, y2)

lines = plt.plot(x,y, x, ym1, x,ym2, 'o')
plt.setp(lines[0], linewidth=4)
plt.setp(lines[1], linewidth=2)
plt.setp(lines[2], markersize=10)

plt.legend(('No mask','Masked if >0,5','masked if <-0.5'),loc='upper right')  # upper lower center  right left center

plt.title('Masked line demo')
plt.show()