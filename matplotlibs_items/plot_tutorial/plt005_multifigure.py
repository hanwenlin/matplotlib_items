#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])


plt.figure(2)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(211)
plt.title('Easy as 1,2,3')
plt.show()