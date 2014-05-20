# Data analysis :
#
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab as pl
#
#Use numpy to load the data contained in the file
#
data = np.loadtxt('bead_medium1.txt')
#
data     # print the data :
#
data[:,3]  #  third column of the datafile
#
data[:,2]  #   second column of the datafile is taken (x)
#
data[:,1]  #   first column of the datafile is taken (t)
#
pl.plot(data[:,1],data[:,2],'ro')       # 1D particle simulation :
pl.xlabel('time')
pl.ylabel('x')
#
pl.plot(data[:,2],data[:,3],"-")         # 2D particle simulation :
pl.xlabel('x')
pl.ylabel('time')
#
delta = diff(data[:,1])
tau = delta # set lag to 0.1
print(tau)

Nlag = 1600 # maximum number of lags to compute
msd = zeros(Nlag)
lags = arange(1,Nlag)

# compute msd
for lag in lags:
    #d = np.diff(data[:,2],n=2)
    #print(d)
    #msd[lag] = mean((d)**2)
    msd[lag] = mean((data[lag:] - data[:-lag])**2)
    
# plot lags against msd : expect a straight a line
plot(lags,msd[1:], ".")
xlabel('lags')
ylabel('Mean Squared Displacement')
#
subplot(211), plot(data[:,3])
subplot(212), plot(data[:,2])
#

