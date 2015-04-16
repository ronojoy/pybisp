from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class WienerProcess:

      def __init__(self, path):
        self.path = path

      def setPrior(self, prior):
        '''priors for parameters'''

      def logProb(self, theta):
        '''analytical expression for the logarithm of the posterior'''
        N = np.size(self.path[:, 1])
        dt = self.path[0, 1] - self.path[0, 0]
        dx2 = sum((self.path[1, 1:] - self.path[1, :-1])**2)
        
        s = -dx2/(4*theta*dt) - np.log(theta)-0.5*(N-1)*np.log(4*theta*np.pi*(dt))
        return s


      def mapEstimate(self, method):
        '''analytical or numerical maximum aposteriori estimate of parameters'''

      def normalEstimate(self):
        '''analytical estimate of parameters assuming asymptotic normality'''

      def posteriorInterval(self, percent):
        '''domain containing p percent of the probability'''

      def plotLogProb(self, extent):
        '''plot of the posterior probability'''
        x = extent*0     # initializing x to be zeros of same size as extent
        
        for i in range(np.size(extent)):
            '''call logProb method and update x'''
            x[i] = self.logProb(extent[i])

        #plotting logProb with extent
        plt.plot(extent, x)
        plt.xlabel('Theta')
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
