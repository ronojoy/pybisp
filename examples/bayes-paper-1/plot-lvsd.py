# Code to plots the Log P vs stiffness of the trap 
#
#

from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pybisp as pb

# read in the data file sampled at 1.5 kHz over 20 seconds
datafile='optical-trap-dataset2.xlsx'
data = pd.ExcelFile(datafile).parse()
sample_path = data.values

# set some useful parameters
dt = 1.0/1500; t = np.arange(0, data.size*dt, dt)

k_B = 1.38064881313131e-17  # Boltzmann constant(N micron/Kelvin)
T = 300                     # temperature(Kelvin)
# MAP estimate assuming an Ornstein-Uhlenbeck process
ou = pb.ou.Inference(sample_path, dt)
L, D, K = ou.mapEstimate() 
k = K * (k_B*T) # physical value of the stiffness (N /micron)
print 'The best estimate for the stiffness is', k, 'N/muM '

# plot logposterior as a heat map with contours showing credible regions
LL, DD = np.meshgrid(np.linspace(L - 40, L + 40, 256), np.linspace(D - 0.01, D + 0.01, 256))
lp = ou.logProb(LL, DD) - ou.logProb(L, D)

c = plt.contourf(LL, DD, lp, cmap=plt.cm.gray);
plt.plot(L, D, 'o', color="#A60628", markersize=12)

f_c = 39.2; L_exp=f_c*np.pi*2
D_exp = 0.17;
print L, D
print 
print L_exp, D_exp
#plt.plot(L_exp, D_exp, 's',  color="#348ABD", markersize=12)
#c = plt.contourf(LL, DD, lp/(np.max(np.abs(lp))), 8, cmap=plt.cm.gray);plt.plot(L, D, 'ro')
#plt.colorbar(c, orientation='horizontal')

#values of chi-squared with 2 dof for 30%, 90% and 99% probability
levels = [-2.41, -4.60, -9.21] 
levels.sort()
CS=plt.contour(LL, DD, lp, levels, cmap=plt.cm.RdBu)
fmt = {}
strs = [ '99%', '90%', '70%', '54%', '54%' ]
for l,s in zip( CS.levels, strs ):
    fmt[l] = s

# Label every other level using strings
plt.clabel(CS,CS.levels[::2],inline=True,fmt=fmt,fontsize=16)


plt.xlabel('$\lambda$ (s$^{-1}$)', fontsize=24)
plt.ylabel('D($\mu$m$^2$ s $^{-1}$) ', fontsize=24);
plt.xticks(np.arange(225, 290, 15), fontsize=20)
plt.yticks(np.arange(0.165, 0.181, 0.005), fontsize=20)
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

plt.savefig('pybispFig1.jpg', dpi=256)
plt.show()
