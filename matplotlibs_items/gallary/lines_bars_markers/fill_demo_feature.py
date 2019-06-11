#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6,100)
y1 = np.sin(x*np.pi)
y2 = np.sin(x*np.pi/3)

#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.fill(x, y1)
# plt.fill(x, y2)

plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)

plt.show()