#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

np.random.seed(0)
mu = 200
sigma = 25
n_bins = 50
x = np.random.normal(mu, sigma, size=100)

fig, ax = plt.subplots(figsize=(8,4))

n, bins, patches = ax.hist(x, n_bins, normed=1, histtype='step', cumulative=True, label='Empirical')

y = mlab.normpdf(bins, mu, sigma).cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

ax.hist(x,  bins=bins, normed=1, histtype='step', cumulative=-1, label='Reversed emp.')

ax.grid(True)
ax.legend(loc='right')
ax.set_title('cumulative step histograms')
ax.set_xlabel('Annual rainfall(mm)')
ax.set_ylabel('Likelihood of occurrence')

plt.show()