#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

partition = [37.2, 33.4, 3.7, 0.6, 25.2]
labels = ['大专', '本科', '硕士', '其它', '中专']

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

explode = [0, 0.1, 0, 0, 0]
plt.pie(partition,explode=explode,labels=labels, colors=['r','b','pink','y','g'],
        autopct='%.1f%%',
        pctdistance=0.8,
        labeldistance=1.2,
        # startangle=180,
        # radius=1
        # counterclock=False,
        wedgeprops={'linewidth':1.5,'edgecolor':'green'},
        textprops={'fontsize':12,'color':'w'},
        # center=(1.8,1.8),
        # frame=1
        )
plt.title('芝麻信用失信用户教育水平分布')
# plt.xlabel('本科')


plt.show()