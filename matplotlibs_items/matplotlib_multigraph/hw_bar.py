#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

railway = [3.11, 2.81, 3.22,3.01, 3.03, 2.99, 3.1, 3.16]
highway = [28.69, 20.74, 31.76, 33.97, 35.0, 35.0, 35.08, 36.27]
airplane = np.array(highway)+np.random.randint(2,6)/10.0
waterway = [33.91, 25.39, 36.83, 39.44, 40.58, 40.9, 40.82, 42.02]

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# plt.bar(range(8), waterway, color='purple', label='水运')
# plt.bar(range(8), airplane, color='k', label='航运')
# plt.bar(range(8), highway, color='g', label='公路')
# plt.bar(range(8), railway, color='r', label='铁路')

plt.bar(range(8), railway, color='r', label='铁路')
plt.bar(range(8), np.array(highway)-np.array(railway), color='g', label='公路', bottom=railway)
plt.bar(range(8), np.array(airplane)-np.array(highway), color='k', label='航运', bottom=highway)
plt.bar(range(8), np.array(waterway)-np.array(airplane), color='purple', label='水运', bottom=airplane)
# 提供bottom参数，其目的就是在某个条形图顶端的基础上，绘制其他条形图，以此类推可以绘制多个堆叠条形图


plt.title('2017年各月份物流运输量')
plt.xticks(range(8), ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jan', 'Jul', 'Aug'])
plt.ylabel('货物量(万吨)')
plt.xlabel('月份')
plt.ylim(0,50)
plt.legend(loc='upper center', ncol=4)      # ncol 图例一行四个

for x,y in enumerate(railway):
    plt.text(x, y-0.2, '%.2f万' %y, ha='center', va='top', color='w')


for x,y in enumerate(waterway):
    plt.text(x, y-0.2, '%.2f万' %y, ha='center', va='top', color='w')


for x,y in enumerate(highway):
    plt.text(x, y/2, '%.2f万' %y, ha='center', va='center')

plt.show()