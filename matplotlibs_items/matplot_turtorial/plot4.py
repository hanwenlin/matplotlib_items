#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2*X)

plt.plot(X, Y+1, color='blue',  alpha=1.00)
plt.fill_between(X, 1, Y+1, color='blue', alpha=0.25)


plt.plot(X, Y-1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y-1,(Y-1)>-1, color='blue', alpha=0.25)
plt.fill_between(X, -1, Y-1, (Y-1)<-1, color='red', alpha=0.25)

plt.show()