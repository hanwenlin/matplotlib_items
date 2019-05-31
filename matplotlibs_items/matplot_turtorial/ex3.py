#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 数据个数
n = 1024
# 均值为0, 方差为1的随机数
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

# 计算颜色值
color = np.arctan2(y, x)
# print(color)
# color = np.arange(0,n)
# 绘制散点图
plt.scatter(x, y, c = color, alpha = 0.5, s=12)
# 设置坐标轴范围
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 不显示坐标轴的值
plt.xticks(())
plt.yticks(())

plt.show()
