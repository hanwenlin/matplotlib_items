#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)

y1 = 2*x +1
plt.figure()
plt.plot(x, y1)

y2 = x**2
plt.figure()
plt.plot(x, y2)

# y2 = x**2
plt.figure(num=5, figsize=(4,4))
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
plt.show()