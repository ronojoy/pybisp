import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab as pl
from __future__ import division


def logprob(D, dx2, dt, N):
    return -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
            
N = 1290
t = arange(N)                  # sampling times
dw = np.random.randn(N)        # Wiener increments
x = np.cumsum(dw)


dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]


D = np.linspace(0.8,1.2, 1028)
#D = np.linspace(0.8,1.2, 1024)


plot(D, logprob(D, dx2, dt, N),'-',lw=1)


xlabel('D')
ylabel('P(D)')
grid('on')

print dx2/(N*dt)
