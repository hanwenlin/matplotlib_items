#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256)
y1 = np.cos(x)
y2 = np.sin(x)

fig = plt.figure(figsize=(10,6))
plt.plot(x, y1, '-', color='red', label='cosine')
plt.plot(x, y2, color='blue', label='sine')
plt.title('cos or sin($-\pi$)')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1,-0.5,0,0.5,1],['-1','-0.5','0','0.5','1'])

# 脊柱，改变坐标轴位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))  # data axes outward
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 添加图例
plt.legend(loc='upper left')

# 注释 annotate
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter([t,], [np.cos(t),], 50, color='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=26,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.65))
plt.show()
