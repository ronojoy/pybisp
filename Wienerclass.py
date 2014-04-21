import numpy as np
import pandas as pd
import pybisp as pb
from __future__ import division
from pandas import DataFrame, read_csv
from pybisp import ReadDataFrame
from pybisp import WienerInference, OrnsteinUhlenbeckInference
#
#Generate data:
#
N = 40                     
t = arange(N)                  # sampling times
dw = np.random.randn(N)        # Wiener increments   
x = np.cumsum(dw)              # Brownian path
#
#Inference for Wiener Process:
#
def ReadDataFrame(data):
    return pd.read_csv('diffusion.csv')

f = open('diffusion.csv', 'wb')             # open the data file
f.write(str(x))
f.write(str(t))                             # write the output as a string
f.close()                                   # Close the file:
data = pb.ReadDataFrame('diffusion.csv')    # read diffusion time series data from csv 
data = pd.read_csv('diffusion.csv')         # Load csv into pandas dataframe
##
def WienerInference(D,dx2,dt,N):
    return -dx2/(2*D*dt) - np.log(D) -0.5*(N-1)*np.log(2*D*np.pi*(dt))
            
dx2 = sum((x[1:] - x[:-1])**2)
dt = t[1] - t[0]
dx = sum((x[1:] - x[:-1])**4)
D = np.linspace(0.8,1.2, 1028)
#
plot(D, WienerInference(D,dx2,dt,N),'r-',lw=2)
#
xlabel('D')
ylabel('P(D)')
grid('on')
print dx2/(N*dt)
print data

# Estimation for the variance:
estimate = -2*(N+1)*(dt)**2/dx
print estimate

