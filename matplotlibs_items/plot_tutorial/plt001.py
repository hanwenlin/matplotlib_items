#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,5])         # x轴范围0-3, figure(1)默认
plt.ylabel('some numbers')
plt.show()

plt.plot([1,2,3,4],[1,4,6,16])
plt.show()