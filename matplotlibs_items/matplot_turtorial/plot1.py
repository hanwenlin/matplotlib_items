#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256)
y1 = np.cos(x)
y2 = np.sin(x)

fig = plt.figure(figsize=(10,6))
plt.plot(x, y1, linestyle='-', linewidth=1, color='red', marker='o', markersize=2, markerfacecolor='red', markeredgecolor='yellow')
plt.plot(x, y2, color='blue')
plt.title('cos or sin($-\pi$)')
# plt.xlim(-4,4)
plt.legend(['y1','y2'],loc='upper left')
plt.xlabel('x')
# plt.xticks(np.linspace(-4,4,17,endpoint=True))
# plt.xticks(np.arange(-np.pi, np.pi+0.02, np.pi/4))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1,-0.5,0,0.5,1])
plt.show()
