from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


class Inference:
    ''' Inference for discretely observed sample paths of the 
        Ornstein-Uhlenbeck process described by the Ito stochastic 
        differential equation

        dx = -lambda x dt + sigma dW

        where lambda is the mean regression rate and sigma
        is the volatility. For physical Brownian motion
        with a friction constant gamma and spring constant k
        at temperature k_BT, the mean regression rate is

        lambda = k/gamma

        and the volatility is

        sigma = sqrt(2k_BT/gamma)

        From the Einstein relation, the diffusion coefficient is

        D = k_BT/gamma

        and it is then convenient to infer D = sigma^2/2 rather than sigma.

        The class is instantiated as

        ou = ou.Inference(sample_path, dt)

        where sample_path is a 1d numpy array of the time series and 
        dt is a float of the sampling interval. 

        This class provides the log posterior probability for the parameters
        lambda and D, their MAP estimates, the error bars, and plots the log
        posterior around the MAP estimate.'''


    def __init__(self, sample_path, dt):
        self.x  = sample_path
        self.N  = sample_path.size
        self.dt = dt

        # compute sufficient statistics
        x = self.x
        self.T1 = np.sum(x[1:]**2)
        self.T2 = np.sum(x[1:]*x[:-1])
        self.T3 = np.sum(x[:-1]**2)
        self.T4 = x[0]*x[0]

    def setPrior(self, choice): 
        pass

    def logProb(self, L, D):
        '''logarithm of the posterior probability of mean regression rate
        and diffusion coefficient'''

        dt = self.dt
        N  = self.N

        T1 = self.T1
        T2 = self.T2
        T3 = self.T3
        T4 = self.T4

        a = np.exp(-L*dt)
        b = 1.0 - np.exp(-2.0*L*dt)

        # log likelihood
        ll1 = ((N-1)/2)*np.log(L/2.0*np.pi*D*b)
        ll2 = (L/2.0*D*b)*(T1 - 2.0*T2*a + T3*a*a)
        ll3 = 0.5 * np.log(L/(2.0*np.pi*D))
        ll4 = (L/2.0*D)*x[0]*x[0]
        ll = ll1 - ll2 + ll3 - ll4

        # log prior
        lpr = 0

        # log posterior
        lp = ll + lpr

        return lp

    def mapEstimate(self):
        '''MAP estimate of mean regression rate and diffusion coefficient'''

        dt = self.dt
        N = self.N

        T1 = self.T1
        T2 = self.T2
        T3 = self.T3
        T4 = self.T4

        # map estimate for lambda
        L0 = np.log(T3/T2)/dt

        a = np.exp(-L0*dt)
        b = 1.0 - np.exp(-2.0*L0*dt)

        # map estimate for D
        D0 = (L0/N) * ( (T1 - 2.0*T2*a + T3*a*a)/b )

        # map estimate for k (in units of k_BT)
        k0 = L0/D0

        return L0, D0, k0

    def errorBar(self):
        '''error bars of the MAP estimates of the mean regression rate and diffusion
        coefficient'''
        pass

    def plotLogProb(self, ll, dd):
        pass

    def plotPath(self):
        '''plot sample path as a time series'''
        t = np.arange(0, dt*N, dt)
        plt.plot(t, self.x)
