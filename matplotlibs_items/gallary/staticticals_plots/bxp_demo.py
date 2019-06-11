#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(937)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')

fig, axes = plt.subplots(nrows=2, ncols=3,figsize=(6,6),sharey=True)

axes[0,0].boxplot(data)
axes[0,0].set_title('Default',fontsize=12)

axes[0,1].boxplot(data, showmeans=True,meanline=True,meanprops={'linestyle':'-','color':'red'})
axes[0,1].set_title('showmeans=True',fontsize=12)

axes[0,2].boxplot(data, showmeans=True,meanline=True)
axes[0,2].set_title('showmeans=True,\nmeanline=True',fontsize=12)

axes[1,0].boxplot(data,showbox=False,showcaps=False)
axes[1,0].set_title('Tufte Style\n(showbox=False,\nshowcaps=False)')

axes[1,1].boxplot(data,notch=True)
# axes[1,1].set_title('notch=True',fontsize=12)

axes[1,2].boxplot(data,showfliers=False)


for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

plt.setp(axes,xticks=[1,2,3,4],xticklabels=labels)

plt.show()