#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 新建figure
fig = plt.figure()

x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])  # 列表或者元祖，离fig的百分比，10%，80%
ax1.plot(x,y,'r')
ax1.set_title('area1')


ax2 = fig.add_axes([0.2,0.6,0.25,0.25])
ax2.plot(x,y,'b')
ax2.set_title('area2')
plt.show()

