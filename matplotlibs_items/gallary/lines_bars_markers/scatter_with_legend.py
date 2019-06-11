#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from numpy.random import rand

fig, ax = plt.subplots()
for color in ['red','green','blue']:
    n = 750
    x,y = rand(2,n)
    scale = 200.0*rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.3, edgecolor='none')

ax.legend(ncol=3,loc='upper center')
ax.grid(True)


plt.show()