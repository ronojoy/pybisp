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

# MAP estimate assuming equipartition
eqp = pb.equipartition.Inference(sample_path)
K = eqp.mapEstimate()
k = K * (k_B*T) # physical value of the stiffness (N /micron)
print 'The best estimate for the stiffness is', k, 'N/muM '

# error bars and posterior probability plots
dK = eqp.errorBar() 
pp = 1e12
k0= K*(k_B*T)*pp
dk0 = k_B*T*dK*pp


# plot logposterior physical units around the '3 sigma' interval
kk = np.linspace(K - 4.0*dK, K + 4.0*dK)
plt.plot(kk*(k_B*T)*pp, eqp.logProb(kk) - eqp.logProb(K), color='black', linewidth=2);
plt.plot(k0, 0, 'o', color="#A60628", markersize=12)
plt.axvspan(k0-3*dk0, k0 + 3*dk0, alpha=0.05, color = 'black')
plt.axvspan(k0-2*dk0, k0 + 2*dk0, alpha=0.1, color = 'black')
plt.axvspan(k0-1*dk0, k0 + 1*dk0, alpha=0.2, color = 'black')

plt.xlabel('k (pN/$ \mu $m)', labelpad=20, fontsize=24);
plt.ylabel('$\Delta$ log posterior', fontsize=24)
plt.xticks(np.arange(5.94, 6.16, .06), fontsize=20)
plt.yticks(np.arange(-4, 1, 1), fontsize=20)
plt.ylim(-4., .5);
plt.xlim(k0-4*dk0, k0+4*dk0)
plt.grid()
#plt.gcf().subplots_adjust(bottom=0.05)
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()
#from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})
#rcParams['xtick.major.pad']='24'
#plt.tick_params(axis='x', which='major', pad=15
#plt.savefig('pybispFig2.jpg', dpi=256)
plt.show()
