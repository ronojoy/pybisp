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

def WienerInference(data1):
    return -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
#
def OrnsteinUhlenbeckInference(data2):
    return((N/2)*np.log(2*sigma**2*dt)-(1/sigma**2)*(x2-x1*exp(-gamma*dt))**2/2*dt+np.log(1/gamma))
#
filename = 'diffusion.csv'                    # Give the filename(e.g.'diffusion.csv' here) in this line :
data = pb.ReadDataFrame(filename)             # read diffusion time series data from csv :
print data
#
N = len(data)                                 # count the number of data points from a given datafile in which the data size can be counted from the file:
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
data1 = {"N":N,"dx2": dx2, "D":D,"dt":dt, "dx":dx}      # Initialise the parameters values here :
print data1
#
data2 = {"sigma":sigma,"gamma":gamma,"dt":dt,"N":N,"x2": x2, "x1":x1}
print data2
#
#Estimate the parameters:(This estimate part should be checked)
#
estimate = pb.WienerInference(data1)
print estimate
#
plot(D, WienerInference(data1),'r.',lw=2)
plt.plot(gamma, OrnsteinUhlenbeckInference(data2),'g',lw=2)
#plot(gamma, OrnsteinUhlenbeckInference(data2),'r',lw=2)
#
xlabel('D')
ylabel('P(D)')
grid('on')

print dx2/(N*dt)
##############################3




