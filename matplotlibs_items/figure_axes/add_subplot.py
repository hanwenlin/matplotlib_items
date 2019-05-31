#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
# 新增figure对象
fig = plt.figure()
#新增子图1 add_subplot参数与subplots相似
ax1 = fig.add_subplot(2,2,1)
ax1.plot(x,x)

#新增子图3
ax3 = fig.add_subplot(2,2,4)
ax3.plot(x,-x)
plt.show()