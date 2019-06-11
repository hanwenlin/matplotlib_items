#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

fig, ax = plt.subplots()

ax.errorbar(x,y, marker='o', markerfacecolor='r', xerr=0.2, yerr=0.4)
plt.show()