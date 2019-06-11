#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
data = np.random.lognormal(size=(37,4), mean=1.5, sigma=1.75)
labels = list('ABCD')
fs = 10

fig, axes =  plt.subplots(nrows=2, ncols=3, figsize=(6,6), sharey=True)
axes[0,0].boxplot(data, labels=labels)
axes[0,0].set_title('Default', fontsize=fs)

axes[0,1].boxplot(data, labels=labels, showmeans=True)
axes[0,1].set_title('showmeans=True', fontsize=fs)

axes[0,2].boxplot(data, labels=labels, showmeans=True, meanline=True)
axes[0,2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)

axes[1,0].boxplot(data,labels=labels, showbox=False, showcaps=False)
tufte_title = 'Tufte Style\n (showbox=False,\nshowcaps=False)'
axes[1,0].set_title(tufte_title, fontsize=fs)

axes[1,1].boxplot(data, labels=labels, notch=True,bootstrap=1000)
axes[1,1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)

axes[1,2].boxplot(data, labels=labels, showfliers=False)
axes[1,2].set_title('showfliers=False', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()

boxporps = dict(linestyle='-.', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')

medianprops = dict(linestyle='-', linewidth=4, color='firebrick')
meanpointprops = dict(marker='D',markeredgecolor='black', markerfacecolor='firebrick')

meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

fig,axes = plt.subplots(nrows=2, ncols=3, figsize=(6,6), sharey=True)
axes[0,0].boxplot(data, boxprops=boxporps)
axes[0,0].set_title('Custom boxprops', fontsize=fs)

axes[0,1].boxplot(data, flierprops=flierprops, medianprops=medianprops)
axes[0,1].set_title('Custome medianprops\nand flierprops', fontsize=fs)

axes[0,2].boxplot(data, whis='range')
axes[0,2].set_title('whis=range', fontsize=fs)

axes[1,0].boxplot(data, meanprops=meanpointprops,meanline=False, showmeans=True)
axes[1,0].set_title('Custome mean\n as point', fontsize=fs)

axes[1,1].boxplot(data, meanprops=meanlineprops, meanline=True, showmeans=True)
axes[1,1].set_title('Custom mean\n as line', fontsize=fs)

axes[1,2].boxplot(data,whis=[15,85])
axes[1,2].set_title('whis=[15,85]\n#percentiles', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.suptitle("I never said they'd be pretty")
fig.subplots_adjust(hspace=0.4)

plt.show()