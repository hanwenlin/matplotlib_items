#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
y = [10,15,23,67,89]

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

xlabels = ['上海','北京','天津','武汉','苏州']

# plt.bar(x,y,width=0.8,color=['y','r'],edgecolor='b',linewidth=4,yerr=3)
bins = 0.4
b1 = plt.bar(x-bins/2,y,width=0.4,color='r')
b2 = plt.bar(x+bins/2,np.array(y)+10,width=bins,color='y')

for i,va in enumerate(y):
    plt.text(i+1-bins/2,va,'%d'%va,horizontalalignment='center',verticalalignment='bottom')

for i,va in enumerate(np.array(y)+10):
    plt.text(i + 1 + bins / 2, va, '%d' % va, horizontalalignment='center', verticalalignment='bottom')
plt.plot(x,y,'g')

plt.xticks(x,xlabels)
#
# plt.text(-3, 20, "function: y = x * x", size = 15, alpha = 0.2)
# plt.text(-3, 40, "function: y = x * x", size = 15,
#          family = "fantasy", color = "r", style = "italic", weight = "light",
#          bbox = dict(facecolor = "r", alpha = 0.2))

# plt.barh(x,width=y,height=0.6)
# plt.yticks(x,xlabels)

plt.show()