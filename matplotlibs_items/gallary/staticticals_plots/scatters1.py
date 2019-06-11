#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

area = np.random.rand(6)*100
marker = ['o',]

plt.scatter(x,y,s=area)

plt.show()