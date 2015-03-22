from __future__ import division
import numpy as np
immport matplotlib.pyplot as plt

class WienerProcess:

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
