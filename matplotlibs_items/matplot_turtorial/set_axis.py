#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

plt.xlim(-1,1)
plt.ylim(0,3)

plt.xlabel(u'这是x轴', fontproperties='SimHei', fontsize=14)
plt.ylabel(u'这是y轴', fontproperties='SimHei', fontsize=14)

plt.xticks(np.linspace(-1,1,5))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',1.5))
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(10)
    label.set_bbox(dict(facecolor='green',edgecolor='None',alpha=0.7))

plt.show()