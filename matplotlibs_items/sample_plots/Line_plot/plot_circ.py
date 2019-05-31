#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))
x = np.arange(-1, 1.01, 0.01)
y1 = np.sqrt(1.0000001-x**2)
y2 = -np.sqrt(1.0000001-x**2)

lines = plt.plot(x,y1,x,y2,linewidth=2)
plt.setp(lines[0],color='red')
# plt.xlim(-1.2,1.2)
plt.show()