#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

p = patches.Rectangle((left,bottom),width,height,fill=False, transform=ax.transAxes, clip_on=False)
ax.add_patch(p)

ax.text(left,bottom,'left top',horizontalalignment='left',verticalalignment='top')
ax.text(left,bottom,'left bottom',horizontalalignment='left',verticalalignment='bottom')
ax.text(right,bottom,'center top',horizontalalignment='center',verticalalignment='top')
ax.text(left,0.5*(top+bottom),'right center',rotation=90,horizontalalignment='right',verticalalignment='center')
ax.text(left,0.5*(top+bottom),'left center',rotation='vertical',horizontalalignment='left',verticalalignment='center')
ax.text(left,top,'rotated\nwith newlines',rotation=45,horizontalalignment='center',verticalalignment='center')
ax.text(0.5*(left+right),0.5*(top+bottom),'middle',verticalalignment='center',horizontalalignment='center',color='red',fontsize=20)


# ax.text(left, bottom, 'left top',horizontalalignment='left',
#         verticalalignment='top', transform=ax.transAxes
#         )
#
# ax.text(left, bottom, 'left bottom',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
#
#
# ax.text(right, top, 'right bottom',
#         horizontalalignment='right',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
#
# ax.text(right, top, 'right top',
#         horizontalalignment='right',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(right, bottom, 'center top',
#         horizontalalignment='center',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(left, 0.5*(bottom+top), 'right center',
#         horizontalalignment='right',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(left, 0.5*(bottom+top), 'left center',
#         horizontalalignment='left',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(0.5*(left+right), 0.5*(bottom+top), 'middle',
#         horizontalalignment='center',
#         verticalalignment='center',
#         fontsize=20, color='red',
#         transform=ax.transAxes)
#
# ax.text(right, 0.5*(bottom+top), 'centered',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(left, top, 'rotated\nwith newlines',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation=45,
#         transform=ax.transAxes)
plt.show()