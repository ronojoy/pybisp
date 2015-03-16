from __future__ import division
import numpy as np

def wiener(D, data, dt):
      N = np.len(data)
      dx = np.diff(data)
      dx2 = np.sum(dx*dx)
      return -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))

def oup(theta, data, dt, a):
      N = np.len(data)
      a2 = a*a
      gamma, D = theta[0], theta[1]
      dx = data[1:] - np.exp(-gamma)*data[-1:]
      dx2 = np.sum(dx*dx)
      B = 1 - np.exp(-2*gamma)
      return 0.5*(N-1)*np.log(gamma/(2*np.pi*D*B*a2)) - gamma *dx2/(2*D*I*a2)


