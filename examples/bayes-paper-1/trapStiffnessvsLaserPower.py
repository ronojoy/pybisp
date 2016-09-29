# Code to plots the laser power vs trap stiffness estimated from Bayes I, II and PSD 
#
#

from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pybisp as pb

laserP  = [10.1, 16.1, 27.2, 31.8, 33.6, 36.8, 43.8]
PSD     = [1.20, 2.26, 3.94, 4.22, 4.40, 4.74, 5.98]
bayes1  = [1.10, 2.23, 3.88, 4.16, 4.48, 4.83, 6.01]
bayes2  = [1.10, 2.23, 3.88, 4.16, 4.48, 4.83, 6.01]

errPSD  = [0.02*1.30, 0.05*2.40, 0.06*3.99, 0.08*4.25, 0.09*4.40, 0.10*4.67, 0.12*5.98] 
ebayes1 = [0.06*1.10, 0.01*2.23, 0.02*3.88, 0.02*4.16, 0.02*4.48, 0.03*4.83, 0.03*6.01]
ebayes2 = [0.06*1.10, 0.05*2.23, 0.05*3.88, 0.02*4.16, 0.02*4.48,0.02*4.83, 0.03*6.01]

##Bayes1
plt.plot(laserP, bayes1, 's', color="g", markersize=6, mec='g', label='Bayes $I$' )
plt.errorbar(laserP, bayes1, ebayes2, fmt='none', ecolor="g" )
slopeInter = np.polyfit(laserP, bayes1, 1)
p = np.poly1d(slopeInter)
plt.plot(laserP, p(laserP), '-', color="g" )

##Bayes2
plt.plot(laserP, bayes2, 'o', mfc='none', markersize=12.5, mec="#A60628", mew=1.5, color="#A60628", label='Bayes $II$')
plt.errorbar(laserP, bayes1, ebayes1, fmt='none', ecolor="#A60628" )
slopeInter = np.polyfit(laserP, bayes2, 1)
p = np.poly1d(slopeInter)
plt.plot(laserP, p(laserP), '-', color="#A60628" )

##PSD
plt.plot(laserP, PSD, 'o', color="#348ABD", mec='none', ms=10, label='PSD')
plt.errorbar(laserP, PSD, errPSD, fmt='none', ecolor="#348ABD"  )
slopeInter = np.polyfit(laserP, PSD, 1)
p = np.poly1d(slopeInter)
plt.plot(laserP, p(laserP), '--', color="#348ABD" )

plt.xlabel('Laser power (mW)', fontsize=24)
plt.ylabel('k(pN/$\mu$m) ', fontsize=24);
plt.xticks(np.arange(8, 45, 7), fontsize=20)
plt.yticks(np.arange(1, 7.2, 1), fontsize=20)
plt.gcf().subplots_adjust(bottom=0.05)
plt.tight_layout()
plt.grid()
plt.legend(loc=2, fontsize=16)
plt.text(24, 1.24, r"Slope from Bayes $I$ and $II$=0.139" "\n" "Slope from PSD=0.135", bbox={'facecolor':'white', 'alpha':0.5, 'pad':4}, fontsize=16)


#plt.savefig('errorBayes1.jpg', dpi=256)
plt.show()
