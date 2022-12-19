# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:50:24 2021

@author: radias
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

mpl.matplotlib_fname()
mpl.rcParams.update(mpl.rcParamsDefault)
plt.rcParams.update({'font.size': 20})
figure(figsize=(15, 15), dpi=600)

data = np.array([
    [15, 35],
    [7.5, 28.5],
    [10,	9],
    [12,	24],
    [13,	30],
    [13.5, 34.5],
    [17.5, 16.5],
    [23,	38.5],
    [23,	16.5],
    [23.5,	25],
    [27,	33.5],
])

x, y = data.T
#plt.plot(x,y)
plt.scatter(x,y, s=500)
#plt.xticks(np.arange(min(x), mplt(x)+1, 1.0))
#plt.xticks([1, 2, 3, 4, 5])    # changing x scale by own
plt.scatter([15],[35],color=['red'], s=800) #change color and size of certain points


# =============================================================================
# 
plt.annotate("Warehouse", (15, 35), xytext=(15.5,36), ha='center', label= 'Warehouse') #Add text label to points
plt.annotate("1", (7.5, 28.5), xytext=(7.5,27.5), ha='center') #Add text label to points
plt.annotate("2", (10,	9), xytext=(10,8.0), ha='center') #Add text label to points
plt.annotate("3", (12,	24), xytext=(12,23), ha='center') #Add text label to points
plt.annotate("4", (13,	30), xytext=(13,29), ha='center') #Add text label to points
plt.annotate("5", (13.5, 34.5), xytext=(13.0,34.0), ha='center') #Add text label to points
plt.annotate("6", (17.5, 16.5), xytext=(17.5,15.5), ha='center') #Add text label to points
plt.annotate("7", (23,	38.5), xytext=(23,37.5), ha='center') #Add text label to points
plt.annotate("8", (23,	16.5), xytext=(23,15.5), ha='center') #Add text label to points
plt.annotate("9", (23.5,	25), xytext=(23.5,	24.0), ha='center') #Add text label to points
plt.annotate("10", (27,	33.5), xytext=(27,	32.5), ha='center') #Add text label to points
# plt.show()
# =============================================================================
#plt.gca.annotate('TEST', xytext=(.2,.1), xy=(.2,.2), 
#             arrowprops=dict(arrowstyle="->", color="blue"))
#plt = plt.gca() #call pltis function


#plt.xticks([]) #remove x axis
#plt.yticks([]) #remove y axis

#ax = axis.pltes()
#plt.pltes.xpltis.set_visible(False) #remove x pltis
#plt.pltes.ypltis.set_visible(False) #remove y pltis
#kwargs1 ={'color':'black' }
#kwargs2 ={'color': 'C1'}
#kwargs3 ={'color': 'C2'}
plt.arrow(15, 35, -0.95, -2.45, head_width=0.6, head_length=0.4, fc='k', label='Route A') #blue/black route start
plt.arrow(15, 35, -1.9, -4.9, head_width=0.00, head_length=0, fc='k')

plt.arrow(13, 30, -2.75, -0.75, head_width=0.6, head_length=0.4, fc='k' )
plt.arrow(13, 30, -5.5, -1.5, head_width=0.00, head_length=0.0, fc='k' )

plt.arrow(7.5, 28.5, 3.75, 3.25, head_width=0.6, head_length=0.4, fc='k' )
plt.arrow(7.5, 28.5, 7.5, 6.5, head_width=0.00, head_length=0.1, fc='k' )


plt.arrow(15, 35, -0.75, -0.25, head_width=0.6, head_length=0.4, fc='C2', color='C2', label='Route B') #arrow for green route
plt.arrow(15, 35, -1.5, -0.5, head_width=0.00, head_length=0.1, fc='k', color='C2')

plt.arrow(13.5, 34.5, 5, -4.75, head_width=0.6, head_length=0.4, fc='C2', color='C2') #arrow 2
plt.arrow(13.5, 34.5, 10, -9.5, head_width=0.00, head_length=0.1, fc='k', color='C2')

plt.arrow(23.5,	25, 1.75, 4.25, head_width=0.6, head_length=0.4, fc='C2', color='C2')
plt.arrow(23.5,	25, 3.5, 8.5, head_width=0.00, head_length=0.1, fc='k', color='C2')

plt.arrow(27,33.5, -2, 2.5, head_width=0.6, head_length=0.4, fc='C2', color='C2')
plt.arrow(27,33.5, -4, 5, head_width=0.00, head_length=0.1, fc='C2', color='C2')

plt.arrow(23,	38.5, -4, -1.75, head_width=0.4, head_length=0.6, fc='C2', color='C2')
plt.arrow(23,	38.5, -8, -3.5, head_width=0.00, head_length=0.1, fc='k', color='C2')


plt.arrow(15, 35, 4, -9.25, head_width=0.6, head_length=0.4, fc='C1', color='C1', label='Route C') #warehouse to 8 orange route start
plt.arrow(15, 35, 8, -18.5, head_width=0.00, head_length=0.1, fc='k', color='C1')

plt.arrow(23, 16.5, -2.75, 0, head_width=0.6, head_length=0.4, fc='C1', color='C1')
plt.arrow(23, 16.5, -5.5, 0, head_width=0.00, head_length=0.1, fc='k', color='C1')

plt.arrow(17.5, 16.5, -3.75, -3.75, head_width=0.6, head_length=0.4, fc='C1', color='C1')
plt.arrow(17.5, 16.5, -7.5, -7.5, head_width=0.00, head_length=0.1, fc='k', color='C1')

plt.arrow(10,	9, 1, 7.5, head_width=0.6, head_length=0.4, fc='C1', color='C1')
plt.arrow(10,	9, 2, 15, head_width=0.00, head_length=0.1, fc='k', color='C1')

plt.arrow(12,	24, 1.5, 5.5, head_width=0.6, head_length=0.4, fc='C1', color='C1')
plt.arrow(12,	24, 3, 11, head_width=0.00, head_length=0.1, fc='k', color='C1')


plt.legend(loc='lower right')

#plt.show()

