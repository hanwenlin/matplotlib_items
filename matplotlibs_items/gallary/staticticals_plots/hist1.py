#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

mu, sigma = 100,15
x = mu+sigma*np.random.randn(100000)
print(x)

n,bins,patches = plt.hist(x,50,density=True,facecolor='g',alpha=0.6)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025,r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])

plt.grid(True)
plt.show()