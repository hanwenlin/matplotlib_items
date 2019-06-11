#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(100)
x2 = np.random.rand(100)+np.random.randint(1,3)/30
x3 = np.random.rand(100)-np.random.randint(1,3)/30

f = plt.boxplot([x1,x2,x3],showfliers=True,showmeans=True,meanline=True,meanprops={'color':'k','linestyle':'-'})



for box in f['boxes']:
    box.set(color='r',lw=2)


plt.show()