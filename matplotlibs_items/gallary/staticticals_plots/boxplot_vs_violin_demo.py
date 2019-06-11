#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4), sharey=True)

axes[1].boxplot(all_data, showfliers=False)
axes[1].set_title('box plot')


axes[0].violinplot(all_data,showmeans=False, showmedians=True)
axes[0].set_title('violin plot')


for ax in axes:
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(all_data))])
    ax.set_xticklabels(['x1','x2','x3','x4'])

# plt.setp(axes, xticks=[y+1 for y in range(len(all_data))], xticklabels=['x1','x2','x3','x4'])
plt.show()