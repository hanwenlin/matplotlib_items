#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

ele_sales = ['天猫', '京东', '中国图书网','当当网','亚马逊']
lowest_price = [33.34, 38.9, 45.4, 39.9, 39.5]

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.barh(ele_sales, lowest_price, align='center', height=0.6, color='pink')
plt.title('不同平台书的最低价比较')
plt.xlim(30,47)
plt.xlabel('价格')
for x,y in enumerate(lowest_price):
    plt.text(y+0.2, x, '%.2f' %y, va='center')



plt.show()