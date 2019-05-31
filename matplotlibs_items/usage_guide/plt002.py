#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()   缺省自动调用figure(1)
x = np.linspace(0,2,100)
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple Plot')
plt.legend(['A','B','C'])
plt.show()

