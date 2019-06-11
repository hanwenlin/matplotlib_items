#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_table('scatter.circRNA.STR_vs_CON.txt')
strs = df['STR']
con = df['CON']

n1 = np.array(con)
n2 = np.array(strs)
conMin, conMax = n1.min(),n1.max()
# x = np.linspace(conMin-1,conMax+1,100)
# print(x)
# plt.plot(x,x+1, linestyle='-', color='k')
# plt.plot(x,x, '-k')
# plt.plot(x,x-1, '-k')
# plt.ylim(conMin-1,conMax+1)
# plt.xlim(conMin-1,conMax+1)

x = [1,4,5,7,9]
y = np.array(x)*2-1

colors = ['r','b','g','k','y']
plt.scatter(x,y, color=colors)
plt.plot(x,y)
plt.show()
