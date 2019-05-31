#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

n = 8
x = np.arange(1,9)
y = np.random.randint(10,35,n)

plt.bar(x,y,width=0.2,color='blue')
plt.plot(x,y/2, color='green',linewidth=10)
plt.show()