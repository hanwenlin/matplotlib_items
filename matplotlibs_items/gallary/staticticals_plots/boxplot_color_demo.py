#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import  matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2)
ax1, ax2 = ax[0], ax[1]
# x1 = np.random.randn(2)
#
# x1 = np.random.uniform(-1,1,50)
# x2 = np.random.uniform(-1.5,1.5,50)
# x3 = np.random.uniform(-2.5,2,50)
# x = [x1,x2,x3]
# ax1.boxplot(x)

np.random.seed(123)
colors = ['pink', 'lightblue', 'lightgreen']
all_data = [np.random.normal(0,std,100) for std in range(1,4)]
bplot1 = ax1.boxplot(all_data, vert=True, patch_artist=True)  # vert竖直排列， patch_artist 填充颜色

bplot2 = ax2.boxplot(all_data, notch=True, vert=True, patch_artist=True)        # notch notch shape
for index,box in enumerate(bplot1['boxes']):
    box.set_facecolor(colors[index])

# colors = ['pink', 'lightblue', 'lightgreen']
# for bplot in  (bplot1,bplot2):
#     for patch, color in zip(bplot['boxes'], colors):
#         patch.set_facecolor(color)

for ax in (ax1,ax2):
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(all_data))])
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')

plt.setp((ax1,ax2), xticks=[y+1 for y in range(len(all_data))], xticklabels=['x1','x2','x3','x4'])

plt.show()