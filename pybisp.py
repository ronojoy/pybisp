from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class WienerProcess:

      def __init__(self, path):
        self.path = path

      def setPrior(self, prior):
        '''priors for parameters'''

      def logLikelihood(self, theta):
        '''analytical expression for the logarithm of the likelihood'''
        N = self.path.shape[0] 
        dt = self.path[0, 1] - self.path[0, 0]
        dx2 = sum((self.path[1, 1:] - self.path[1, :-1])**2)
        #Wiener process likelihood
        s = -dx2/(4*theta*dt) - np.log(theta)-0.5*(N-1)*np.log(4*theta*np.pi*(dt))
        return s


      def mapEstimate(self, method):
        '''analytical or numerical maximum aposteriori estimate of parameters'''

      def normalEstimate(self):
        '''analytical estimate of parameters assuming asymptotic normality'''

      def posteriorInterval(self, percent):
        '''domain containing p percent of the probability'''

      def plotLogProb(self, theta):
        '''plot of the posterior probability'''
        logP = np.zeros_like(theta) 

        for i in range(np.size(theta)):
            '''call logProb method'''
            logP[i] = self.logProb(theta[i])

        #plot logProb against theta 
        plt.plot(theta, logP)
        plt.xlabel('theta')
        plt.ylabel('logProb')
        plt.show()


class OrnsteinUhlenbeckProcess:

      def __init__(self, path):
        self.path = path

      def setPrior(self, prior):
        '''priors for parameters'''

      def logProb(self,theta):
        '''analytical expression for the logarithm of the posterior'''

      def mapEstimate(self, method):
        '''analytical or numerical maximum aposteriori estimate of parameters'''

      def normalEstimate(self):
        '''analytical estimate of parameters assuming asymptotic normality'''

      def posteriorInterval(self, percent):
        '''domain containing p percent of the probability'''

      def plotLogProb(self, extent):
        '''plot of the posterior probability'''
