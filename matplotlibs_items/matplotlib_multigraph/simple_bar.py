#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

city = ['北京','天津','上海','重庆']
gdp = [12406.8,9386.87,13908.57,9143.64]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# plt.rcParams['font.family'] = ['sans-serif']
# plt.rcParams['font.sans-serif'] = ['SimHei']


plt.bar(range(4),gdp)
plt.xticks([0,1,2,3],city)
plt.title('四大直辖市GDP比较')
for x,y in enumerate(gdp):
    plt.text(x,y+100,'%s'%round(y,1),ha='center')

plt.show()
