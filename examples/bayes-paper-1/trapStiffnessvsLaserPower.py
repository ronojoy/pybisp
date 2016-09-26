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

errPSD  = [0.15*1.30, 0.12*2.40, 0.15*3.99, 0.19*4.25, 0.25*4.40, 0.25*4.67] 
ebayes1 = [0.10*1.10, 0.12*2.23, 0.15*3.88, 0.15*4.16, 0.19*4.48, 0.20*4.83]
ebayes2 = [0.10*1.10, 0.12*2.23, 0.15*3.88, 0.15*4.16, 0.19*4.48, 0.20*4.83]

plt.plot(laserP, PSD, 'o-', color="#348ABD" )
plt.errorbar(laserP, PSD, errPSD, color="#348ABD", label='PSD')

plt.plot(laserP, bayes1, 'd-', color="#A60628" )
plt.errorbar(laserP, bayes1, ebayes1, color="#A60628", label='Bayes I')

#plt.plot(laserP, bayes2, 'd-', color="#A60628" )
#plt.errorbar(laserP, bayes2, ebayes1, color="#A60628", label='Bayes 2')

plt.xlabel('Laser power (mW)', fontsize=24)
plt.ylabel('k$(\mu Nm^{-1}$) ', fontsize=24);
plt.xticks(np.arange(9, 40, 7), fontsize=20)
plt.yticks(np.arange(1, 5.2, 1), fontsize=20)
plt.gcf().subplots_adjust(bottom=0.05)
plt.tight_layout()
plt.grid()
plt.legend(loc=2, fontsize=20)
plt.savefig('errorBayes1.jpg', dpi=256)
plt.show()
