#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

plt.figure()

plt.vlines(3, 1, 5, color='r', linestyles='--', label='vlines')
plt.hlines(3, 2, 5,label='hlines')

plt.grid(True,axis='y',color='r')
# plt.fill("time", "signal",
#         data={"time": [0, 1, 2], "signal": [0, 1, 0]})
# plt.fill([0,1,3,2],[1,4,5,2],color='r')
x = [0,1,3,2]
y = [1,4,5,2]
plt.plot(x,y)
plt.fill([1,2,3],[2,3,5])

plt.legend(loc='upper left')
plt.show()