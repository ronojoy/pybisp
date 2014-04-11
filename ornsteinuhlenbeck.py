import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab as pl
from __future__ import division

def logprob(sigma,gamma,dt,N,x2,x1):
    return((N/2)*np.log(2*sigma**2*dt)-(1/sigma**2)*(x2-x1*exp(-gamma*dt))**2/2*dt+np.log(1/gamma))

    
            
N = 1290
t = arange(N)                  # sampling times
dw = np.random.randn(N)        # Wiener increments
x = np.cumsum(dw)
sigma = 0.01


dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
#x1 = (x[:-1])**2
x1 = (x[:-1])
x2 = x[1:]


gamma = np.linspace(0.2,3.9, N-1)

plot(gamma, logprob(sigma,gamma,dt,x2,x1,N),'-',lw=1)


xlabel('gamma')
ylabel('P(gamma)')
grid('on')
