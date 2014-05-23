# INCOMPLETE CODE : To be rewritten:
#
Bayesian inference for the estimation of D and variance in Wiener Process:
#
import numpy as np
import pandas as pd
import pybisp as pb
from __future__ import division
from pandas import DataFrame, read_csv
from pybisp import ReadDataFrame
from pybisp import WienerInference, OrnsteinUhlenbeckInference
import matplotlib.pyplot as plt


N = 1028
t = arange(N) # sampling times
dw = np.random.randn(N) # Wiener increments
x = np.cumsum(dw) # Brownian path

dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
dx = sum((x[1:] - x[:-1])**4)
dx2 = sum((x[1:] - x[:-1])**2)
D = np.linspace(0.8,1.2, 1028)


class estimation():                                              # class object : estimate
    
     
    def __init__(self,posterior,variance):                     # Constructor for the class : Initialisation :
        self.posterior = posterior
        self.variance = variance
        
    
                
    def WienerInference(data):                                   # Function returns the posterior and variance :
        return estimation(posterior,variance)
    
    
posterior = -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
variance  = -2*(N+1)*(dt)**2/dx    

       
# 
x = estimation(posterior,variance)                                  # Instantiate the class :
print x.posterior
print x.variance

filename = 'diffusion.csv'   
data = pb.ReadDataFrame(filename)
#print data
estimate = pb.WienerInference(data)
print estimate

###
INCOMPLETE CODE : TO BE REWRITTEN :
#########
