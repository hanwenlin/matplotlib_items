#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y1 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)
y2 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(x, y1, facecolor='blue', edgecolor='white')
plt.bar(x, -y2, facecolor='red', edgecolor='white')

for x0,y0 in zip(x,y1):
    plt.text(x0+0.04,y0+0.03, '%.2f'%y0, ha='center', va='bottom')

#
for x0,y0 in zip(x,-y2):
    plt.text(x0+0.04, y0-0.03,'%.2f'%y0, ha='center', va='top')

plt.ylim(-1.25,1.25)
plt.show()