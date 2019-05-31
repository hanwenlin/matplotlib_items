#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from  matplotlib import gridspec
import numpy as np

fig = plt.figure()
x = np.array([1,2,3,4,5,6])
y = x**2

gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,0:2])
ax3 = plt.subplot(gs[2,2:])

ax1.plot([1,4],[12,6])
ax2.plot(x, y)
ax3.plot(x,-y+2)


plt.show()