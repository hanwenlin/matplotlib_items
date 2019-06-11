#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
# ax1.plot(x, y, marker='o', markersize=12)
# ax1.errorbar(x,y, yerr=x/4)
#
# ax2.scatter(x, y )
# ax2.errorbar(x, y, xerr=x/4,fmt='o')

error = 0.1+0.2*x
ax1.errorbar(x,y, yerr=error, fmt='-o')
ax1.set_title('variable,symmetric error')

lower_error = 0.4*error
upper_error = error
asymmetric_error = [lower_error, upper_error]

ax2.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax2.set_title('variable,asymmetric error')
ax2.set_yscale('log')

plt.show()
