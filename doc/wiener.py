#Bayesian inference for the estimation of D and variance in Wiener Process not using CLASS in ipython:
#
import numpy as np
import pandas as pd
import pybisp as pb
from __future__ import division
from pandas import DataFrame, read_csv
from pybisp import ReadDataFrame
from pybisp import WienerInference, OrnsteinUhlenbeckInference
import matplotlib.pyplot as plt
#
def ReadDataFrame(filename):
    return pd.read_csv(filename)

def WienerInference(data2):
    posterior = -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
    variance = -2*(N+1)*(dt)**2/dx
    return (posterior,variance)
#
#
filename = 'diffusion.csv'                    # Give the filename(e.g.'diffusion.csv' here) in this line :
data = pb.ReadDataFrame(filename)             # read diffusion time series data from csv :
data1 = pd.read_csv(filename)
print data1
#
N = len(data1)                                 # count the number of data points from a given datafile in which the data size can be counted from the file:
print N
#
#
t = arange(N)                                 # sampling times
dw = np.random.randn(N)                       # Wiener increments
x = np.cumsum(dw)                             # Brownian path

dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
dx = sum((x[1:] - x[:-1])**4)
dx2 = sum((x[1:] - x[:-1])**2)
D = np.linspace(0.8,1.2, 1028)
#print dx2
#
#
data2 = {"N":N,"dx2": dx2, "D":D,"dt":dt, "dx":dx}      # Initialise the parameters values here :
print data2
#
#Estimate the parameters:(This error part to be rewritten)
#
estimate = pb.WienerInference(data2)
print estimate
#






