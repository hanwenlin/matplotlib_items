#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,500)
y = np.sin(4*np.pi*x)*np.exp(-5*x)

fig, ax = plt.subplots()

# ax.plot(x,y)
ax.fill(x, y, zorder=10)
ax.grid(True, zorder=10)
ax.set_xlim(0.0,1.0)

plt.show()