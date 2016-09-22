from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


class Inference:
    '''Inference of the stiffness k of a harmonic potential from the histogram
       of positions of a Brownian particle confined in that potential'''
    

    def __init__(self, data):
        self.x  = data
        self.N  = data.size
        
        # compute sufficient statistics
        self.T = np.sum( self.x**2 ) 


    def logProb(self, k):
        '''logarithm of the posterior probability of the stiffness''' 

        N = self.N
        T = self.T
        
        lp1 = (N/2) * np.log(k/(2*np.pi)) 
        lp2 = 0.5 * k * T

        return lp1 - lp2

    def mapEstimate(self):
        '''MAP estimate of mean regression rate and diffusion coefficient'''

        N = self.N
        T = self.T
        
        # map estimate for k 
        k0 = N/T

        return k0

    def errorBar(self):
        '''error bars of the MAP estimates of mean regression rate and diffusion
        coefficient'''
        
        N = self.N
        T = self.T

        # MAP estimate of spring constant
        k0 = N/T

        # error bar of the MAP estimate
        sigma0 = k0/np.sqrt(N)

        return sigma0


    def plotLogProb(self, interval=3):
        ''' plot the log posterior in a Bayesian credible interval, chosen by default as 3 sigma'''
        
        k0  = self.mapEstimate()
        dk0 = self.errorBar()

        eps = 0.001 # offset for plotting
        k = np.linspace(k0 - interval*dk0, k0 + interval*dk0, 128)
        lp = self.logProb(k) - self.logProb(k0) + eps
        
        #plt.rc('text', usetex=True)
        plt.plot(k, lp, color='blue')
        plt.plot(k0, 0, 'o', color='red')
        plt.grid()
        plt.axvspan(k0-3*dk0, k0 + 3*dk0, alpha=0.1, color = 'black')
        plt.axvspan(k0-2*dk0, k0 + 2*dk0, alpha=0.2, color = 'black')
        plt.axvspan(k0-1*dk0, k0 + 1*dk0, alpha=0.3, color = 'black')
        plt.xlabel('$k/k_BT$')
        plt.ylabel('$\Delta$ log posterior')
        plt.show()

