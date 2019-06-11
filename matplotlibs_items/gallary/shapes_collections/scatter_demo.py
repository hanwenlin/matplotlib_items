#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
print(colors)
area = np.pi*(15*np.random.rand(N))**2

plt.scatter(x, y, c=colors, alpha=0.5,s=area)

plt.show()