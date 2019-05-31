#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()          # 一个fig对象就是一个画图板
fig.suptitle('No axes on this figure')
fig,ax_lst = plt.subplots(2,2)
fig.suptitle('four figure in it')



plt.show()