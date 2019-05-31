#!/usr/bin/env python
#-*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,100)
fig,axes = plt.subplots(2,2)

ax1,ax2,ax3,ax4 = axes[0,0],axes[0,1],axes[1,0],axes[1,1]

ax1.plot(x,x)

ax2.plot(x,-x)

ax3.plot(x,x**2)
ax3.grid(color='r',linestyle='--',linewidth=1)

ax4.plot(x,np.log(x))

# fig.show()
plt.show()