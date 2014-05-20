## Bayesian Inference for the Wiener Process using OOP is incomplete:
#
import numpy as np
import pandas as pd
import pybisp as pb
from __future__ import division
from pandas import DataFrame, read_csv
from pybisp import ReadDataFrame
from pybisp import WienerInference, OrnsteinUhlenbeckInference
#
#


class Inference():                                              # class object : Inference
    
     
    def __init__(self,posterior,variance):                     # Constructor for a class :
        self.posterior = posterior
        self.variance = variance
                        
          
    def ReadDataFrame(self,filename):                           # Function returns the dataframe of the datafile :
        return pd.read_csv(filename)
       
    def WienerInference(self,D,dx2,dx,dt,N):                         # Function returns the posterior and variance :
        posterior = -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
        variance  = -2*(N+1)*(dt)**2/dx
        return Inference(posterior,variance) 
        
N = 60
t = arange(N) # sampling times
dw = np.random.randn(N) # Wiener increments
x = np.cumsum(dw) # Brownian path

dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
dx = sum((x[1:] - x[:-1])**4)
dx2 = sum((x[1:] - x[:-1])**2)
D = np.linspace(0.8,1.2, 1028)
#
# Code to be checked and rewritten by by Vanitha.
        
