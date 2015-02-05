import numpy as np
from __future__ import division

def wiener(D, dx2, dt, N):
      return -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))

def oup():
    ## Sudipta will add the logprob calculation here
    pass

