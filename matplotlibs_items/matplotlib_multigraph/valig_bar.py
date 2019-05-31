#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

city = ['北京','上海','香港','深圳','广州']
num_2016 = [15600, 12700, 11300, 4270, 3620]
num_2017 = [17400, 14800, 12000, 5200, 4020]
bar_width = 0.45

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.bar(range(5),num_2016,color='blue', alpha=0.8, label='2016',width=bar_width)
plt.bar(np.arange(5)+bar_width,num_2017,color='red',label='2017',width=bar_width)


plt.xticks(np.arange(5)+bar_width/2,city)
plt.xlabel('Top5城市')
plt.ylabel('家庭数量')
plt.title('亿万财富家庭数Top5城市分布')
plt.legend()

for x,y in enumerate(num_2016):
    plt.text(x,y+3,'%d' %y, ha='center',va='bottom')

for x,y in enumerate(num_2017):
    plt.text(x+bar_width,y+3,'%d'%y, ha='center',va='bottom')


plt.show()