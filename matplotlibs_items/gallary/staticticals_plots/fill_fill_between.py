#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

plt.fill([1,2,4],[3,4,9])
plt.fill_between([1,4],[3,4],[1,2],color='g',interpolate=False,step='mid')


plt.show()