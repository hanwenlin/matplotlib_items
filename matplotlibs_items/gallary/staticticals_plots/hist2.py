#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y = [23,24,45,32,67,24,56,89,12,57,78,34,88,47,57,59,25,60,49,78,72,35,82,19,35,39,48,60,79]

plt.hist(y,normed=1,bins=40,range=(20,70),histtype='bar',align='left',stacked=False)
s = pd.Series(np.random.randn(1000))
s.plot(kind='kde')

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

plt.show()