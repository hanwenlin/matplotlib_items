#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
# ax.yaxis.tick_left() # only ticks on the left side

plt.show()