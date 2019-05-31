#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

n = 20
z = np.random.uniform(0,1,n)

plt.pie(z,explode=z*0.05, colors=['%f' %(i/float(n)) for i in range(n)])
plt.gca().set_aspect('equal')
plt.show()