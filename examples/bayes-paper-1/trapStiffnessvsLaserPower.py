# Code to plots the laser power vs trap stiffness 
#
#

from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pybisp as pb

laserP  = [10.1, 16.1, 27.2, 31.8, 33.6, 36.8]
PSD     = [1.30, 2.40, 3.99, 4.25, 4.40, 4.67]
bayes1  = [1.10, 2.23, 3.88, 4.16, 4.48, 4.83]
bayes2 = [1.10, 2.23, 3.88, 4.16, 4.48, 4.83]

e2=0.00577
errPSD  = [0.15*1.30, 0.12*2.40, 0.15*3.99, 0.19*4.25, 0.25*4.40, 0.25*4.67] 
ebayes1 = [e2*1.10, e2*2.23, e2*3.88, e2*4.16, e2*4.48, e2*4.83]
ebayes2 = [e2*1.10, e2*2.23, e2*3.88, e2*4.16, e2*4.48, e2*4.83]



plt.plot(laserP, bayes1, 'o-', mfc='none', markersize=12.5, mec="#A60628", mew=1.5, color="#A60628", label='Bayes $I$')
plt.errorbar(laserP, bayes1, ebayes1, color="#A60628")

plt.plot(laserP, bayes2, 's-', color="g", markersize=6.4, mec='g', label='Bayes $II$' )
plt.errorbar(laserP, bayes2, ebayes2, color="g")

plt.plot(laserP, PSD, '*-', color="#348ABD" , ms=10, label='PSD')
plt.errorbar(laserP, PSD, errPSD, color="#348ABD")

plt.xlabel('Laser power (mW)', fontsize=24)
plt.ylabel('k(pN/$\mu$m) ', fontsize=24);
plt.xticks(np.arange(8, 40, 7), fontsize=20)
plt.yticks(np.arange(1, 5.2, 1), fontsize=20)
plt.gcf().subplots_adjust(bottom=0.05)
plt.tight_layout()
plt.grid()
plt.legend(loc=2, fontsize=20)
plt.savefig('errorBayes1.jpg', dpi=256)
plt.show()
