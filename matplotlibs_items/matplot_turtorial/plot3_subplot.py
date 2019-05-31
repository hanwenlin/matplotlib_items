#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = plt.subplot(G[1,:-1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = plt.subplot(G[-1,0])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = plt.subplot(G[-1,-2])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

#plt.savefig('../figures/gridspec.png', dpi=64)
plt.show()

fig,axs = plt.subplots(2,2)
ax1 = axs[0,0]
ax1.plot([1,2],[4,6])
ax1.set_xlabel('X')
ax1.set_title('first graghy')
plt.show()
