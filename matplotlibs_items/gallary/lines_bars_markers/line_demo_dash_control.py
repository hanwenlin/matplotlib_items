#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

fig, ax = plt.subplots()
dashes = [10,5, 100,5]
line1, = ax.plot(x, np.sin(x*np.pi/3))          # dashes  实体长度10，空5，实100，空5
line1.set_dashes(dashes)

ax.plot(x, -np.sin(x*np.pi/3), dashes=[30,5,10,15])

ax.legend(['Dashes set retroactively', 'Dashes set proactively'], loc='lower right')

plt.show()