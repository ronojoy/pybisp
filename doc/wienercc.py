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



t = arange(N) # sampling times
dw = np.random.randn(N) # Wiener increments
x = np.cumsum(dw) # Brownian path

dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
dx = sum((x[1:] - x[:-1])**4)
dx2 = sum((x[1:] - x[:-1])**2)
D = np.linspace(0.8,1.2, 1028)


class Estimation():                                                          # class object : estimate
       
     
    def __init__(self,filename, N):                                          # Constructor for the class : Initialisation :
        self.filename = filename
        self.N = N
        
    
                
    def WienerInference(self,N,dx2,dx,dt):                                   # Function returns the posterior and variance :
        return Estimation(posterior,variance)
    
#
filename = 'diffusion.csv'
data = pb.ReadDataFrame(filename)
print data
# 
x = Estimation('diffusion.csv',50)                                            # Instance
x.WienerInference(posterior,variance)                                         # Method 
#
posterior = -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
variance  = -2*(N+1)*(dt)**2/dx 
x = Estimation(posterior,variance)                                           
print x.posterior
print x.variance

estimate = pb.WienerInference(data)
print estimate

###
INCOMPLETE CODE : TO BE REWRITTEN :
#########
