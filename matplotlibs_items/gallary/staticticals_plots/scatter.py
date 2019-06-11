#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,1)
plt.scatter(x,x,s=20)
plt.scatter(x[:3],[2,5,6],s=[10,20],c=[0.1,0.2,4])        # (10, 20, 10..) 三个点大小
# plt.scatter(x,x**2,s=[20,40],c=['r','g','y'])

# a,b=plt.subplots(3,3)
# col=['c', 'b', 'g', 'r', 'c', 'm']
# colq=['c', 'b']
# b[0,2].scatter(range(6),range(6),s=range(5,50,5),c=col)
# #显示6个点，颜色'c', 'b', 'g', 'r', 'c', 'm'
# b[0,2].scatter(range(0,10,2),range(6,16,2),s=range(5,50,5),c=colq*2+['g'])
# #显示5个点，颜色'c', 'b'，'c', 'b'，'c'



plt.show()
