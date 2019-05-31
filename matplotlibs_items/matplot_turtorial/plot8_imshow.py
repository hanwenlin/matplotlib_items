#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,3*n)

X,Y = np.meshgrid(x,y)
plt.imshow(f(X,Y),interpolation='bicubic',cmap='bone',origin='lower')
plt.colorbar(shrink=0.8)
plt.xticks([])

plt.show()