#!/usr/bin/env python
#-*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(100)
plt.subplot(221)            # 221 subplot(2,2,1) 布局是2*2的图，1是第一个图，必须是三位数，还有参数，sharex,sharey..
plt.plot(x,np.sin(x))


plt.subplot(222)
plt.plot(x,-x)


plt.subplot(223)
plt.plot(x,x**2)
plt.grid(color='r',linestyle='--',linewidth=1,alpha=0.3)

plt.subplot(224)
plt.plot(x,np.log(x))
plt.show()
