# Estimating approximate likelihood inference for the parameters of the one dimensional drift-diffusion process:
# This work is under progress:
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab as pl
from __future__ import division
#
#
The one dimensional drift-diffusion process is described by the following stochastic differential equation: 
dx=adt+2D−−−√dW for which the Fokker-Planck equation is ∂P∂t=D∂2P∂x2−a∂P∂x.
a is a drift and W is a wiener process which models white noise.
The transition probability density is given by P(x,t)=12πDt√exp−(x−at)22Dt.
The exact solution is the Gaussian with mean and variance given by ⟨x(t)⟩=∫−∞∞xp(x,t)dx = at, ⟨x2⟩−⟨x⟩2 = Dt so that the transition probability density is given by P(x,t)=12πDt√exp−(x−at)22Dt. 
The parameters are a=⟨x(t)⟩t, D=⟨x2⟩−⟨x⟩2t. The parameter in this process is D and a.
