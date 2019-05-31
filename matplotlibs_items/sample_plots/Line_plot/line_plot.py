#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2,0.025)
y = np.sin(x*np.pi*2)+1

fig = plt.figure()

plt.plot(x, y, linestyle='-', color='#000000', marker='o', linewidth=2, markersize=14, label='line 1',markerfacecolor='yellow')
# plt.plot(x, y, 'o-r', linewidth=2, markersize=14, label='line 1',markerfacecolor='yellow')
plt.title('Sin plot')
plt.xlabel('x')
plt.ylabel('y')
# plt.xlim(0,2)
# plt.ylim(0,2)
plt.show()
