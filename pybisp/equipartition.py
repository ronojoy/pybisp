from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


class inference:
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


    def plotLogProb(self):
        
        k0 = self.mapEstimate()
        sigma0 = self.errorBar()

        k = np.linspace(k0 - 5*sigma0, k0 + 5*sigma0, 128)
        lp = self.logprob(k)

        plt.plot(k, lp)
