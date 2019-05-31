#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,2))
ax.set_title('Cap style')

for x, style in enumerate(['butt','round','projecting']):
    ax.text(x,1,style)
    xx = [x, x+0.5]
    yy = [0, 0]
    ax.plot(xx, yy, lw=12, color='tab:blue', solid_capstyle=style)
    ax.plot(xx, yy, lw=1, color='black')
    ax.plot(xx, yy, 'o', color='tab:red', markersize=3)
ax.text(2, 0.7, '{default}')

ax.set_ylim(-0.5, 1.5)
ax.yaxis.set_visible(False)
plt.show()