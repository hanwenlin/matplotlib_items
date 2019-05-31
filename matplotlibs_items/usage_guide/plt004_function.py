#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def myplotter(ax, data1, data2, param_dict):

    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4,100)
fig, ax = plt.subplots(1,1)
myplotter(ax, data1, data2, {'marker':'x'})
plt.show()

fig, ax = plt.subplots(1, 2)
ax1, ax2 = ax
myplotter(ax1, data1, data2, {"marker":"x"})
myplotter(ax2, data3, data4, {"marker":"o"})
plt.show()

# marker 'o' 'x' ??