#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t,s,lw=2)

ax.annotate('local max',xy=(2,1), xytext=(3,1.5),xycoords='data',
            arrowprops=dict(facecolor='r',shrink=0.05,edgecolor='yellow',headwidth=8)
            )

ax.set_ylim(-1.25,2)

plt.show()