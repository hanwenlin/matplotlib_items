#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# x = [3.4, 11.5, 10.6, 11.8, 12.7]
# y = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
#
# plt.barh(y, x)
# plt.xlim(0,14)
# plt.xlabel('Performance')
# plt.title('How fast do you want to go today?')

plt.rcdefaults()
fig, ax = plt.subplots()

people = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
y_pos = np.arange(len(people))

performance = 3+10*np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center', color='green', ecolor='black')  # xerr yerr是误差那个直线
# ax.barh(y_pos, performance,  align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)

ax.invert_yaxis()                   # 从上往下读，上面的是0，1，...
ax.set_label('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()