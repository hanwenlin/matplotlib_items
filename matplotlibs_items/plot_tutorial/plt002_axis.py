#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4],[1,4,9,16],'ro',alpha=0.5)     # plot参数主要，x,y 颜色线性(分别一个字母，可以合并),还有其它参数
plt.axis([0,6,0,20])                              # 设置x,y轴范围
plt.show()


t = np.arange(0.,5.,0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()