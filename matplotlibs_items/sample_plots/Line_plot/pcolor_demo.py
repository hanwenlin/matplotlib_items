#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

z = np.random.rand(6,10)

fig, (ax0,ax1) = plt.subplots(2,1)

c = ax0.pcolor(z)
ax0.set_title('default:no edges')


ax1.pcolor(z, edgecolor='k', linewidth=4)
ax1.set_title('thick edges')

plt.show()

dx, dy = 0.15, 0.05
y,x =np.mgrid[slice(-3,3+dy,dy),slice(-3,3+dx,dx)]

z = (1-x/2.+x**5+y**3)*np.exp(-x**2-y**2)
z =z[:-1,:-1]
z_min,z_max = -np.abs(z).max(),np.abs(z).max()

fig, axs =plt.subplots(2,2)
ax = axs[0,0]
c = ax.pcolor(x,y,z,cmap='RdBu',vmin=z_min,vmax=z_max)
ax.set_title('pcolor')
ax.axis([x.min(),x.max(),y.min(),y.max()])
fig.colorbar(c,ax=ax)

ax=axs[0,1]
c = ax.pcolor(x,y,z,cmap='RdBu',vmin=z_min,vmax=z_max)
ax.set_title('pcolormesh')
ax.axis([x.min(),x.max(),y.min(),y.max()])
# fig.colorbar(c,ax=ax)

ax = axs[1, 0]
c = ax.imshow(z, cmap='RdBu', vmin=z_min, vmax=z_max,
              extent=[x.min(), x.max(), y.min(), y.max()],
              interpolation='nearest', origin='lower')
ax.set_title('image (nearest)')
fig.colorbar(c, ax=ax)

ax = axs[1, 1]
c = ax.pcolorfast(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolorfast')
fig.colorbar(c, ax=ax)

plt.show()

N = 100
X, Y = np.mgrid[-3:3:complex(0,N),-2:2:complex(0,N)]

Z1 = np.exp(-(X)**2 - (Y)**2)
Z2 = np.exp(-(X*10)**2-(Y*10)**2)
Z = Z1+50*Z2

fig, (ax0,ax1) = plt.subplots(2,1)

c = ax0.pcolor(X,Y,Z,norm=LogNorm(vmin=Z.min(),vmax=Z.max()),cmap='PuBu_r')

fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X,Y,Z,cmap='PuBu_r')
fig.colorbar(c,ax=ax1)
plt.show()