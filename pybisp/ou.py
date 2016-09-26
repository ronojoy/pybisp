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
        ll1 = ((N-1)/2)*np.log(L/(2.0*np.pi*D*b))
        ll2 = (L/(2.0*D*b))*(T1 - 2.0*T2*a + T3*a*a)
        ll3 = 0.5 * np.log(L/(2.0*np.pi*D))
        ll4 = (L/(2.0*D))*T4
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

    def errorBar(self, L, D):
        '''error bars of the MAP estimates of the mean regression rate and diffusion
        coefficient'''
        dt = self.dt
        N  = self.N
 
        T1 = self.T1
        T2 = self.T2
        T3 = self.T3
        T4 = self.T4
 
        a = np.exp(-L*dt)
        b = 1.0 - np.exp(-2.0*L*dt)
        D2 = D*D;  L2 = L*L;   b2 = b*b;
        D3 = D2*D; L3 = L2*L;  b3 = b2*b;
 
        del2 = (T1 - 2.0*T2*a + T3*a*a) 
        ddp  = (T2 - a*T3)*dt*a               # derivative of delta and delta
        dpdp = dt*dt*a*a*T3
        dppd = -dt*dt*a*(T2 - a*T3)
        bP   = 2*dt*a*a                       #derivative of b wrt L
        bPP  = -2*dt*bP                       #double derivative wrt L

        dbP  = 2*ddp/b - bP*del2/b2
        dbPP = 2*(dpdp+dppd)/b - 4*ddp*bP/b2 - bPP*del2/b2 + 2*bP*bP*del2/b3
        nn   = (N-1)/2
 
        h11 = nn*(-1/L2 + bP*bP/b2 - bPP/b) - 0.5/L2  - dbP/D - 0.5*L*dbPP/D
        h12 = del2/(2*D2*b) + L/(2*D2)*dbP + 0.5*T4/D2
        h22 = nn/D2 - (L/D3)*(del2/b-T4)  + 0.5/D2
 
        from numpy import linalg as LA 
        J=np.zeros((2, 2), dtype=float)
        J[0, 0] = -h11 
        J[0, 1] = -h12
        J[1, 0] = -h12
        J[1, 1] = -h22
        eigVals, eigVecs = LA.eig(J)
        return 1/eigVals

    def plotLogProb(self, L, D, level=[60, 90, 99], gridN=64):
        ''' plotting log prob based on chi squared test'''
      
        from scipy import stats, optimize
        maxpValue = stats.chi2.ppf(q=0.01*np.max(level), df = 2)
        chiSq = np.zeros(len(level), dtype=float)

        ''' determine bounds of L''' 
        def rhsL(r):
            v = self.logProb(r, D) - self.logProb(L, D)+maxpValue
            return v
        r=L*1.01
        sol = optimize.root(rhsL, r, method='krylov')
        dL=1.4*np.abs(L-sol.x)

        ''' determine bounds of D''' 
        def rhsD(r):
            v = self.logProb(L, r) - self.logProb(L, D)+maxpValue
            return v
        r=D*1.01
        sol = optimize.root(rhsD, r, method='krylov')
        dD=1.4*np.abs(D-sol.x)
         
        xx = np.linspace(L-dL, L+dL, gridN)  
        yy = np.linspace(D-dD, D+dD, gridN)  
        LL, DD = np.meshgrid(xx, yy)
        lp = self.logProb(LL, DD) - self.logProb(L, D)

        c = plt.contourf(LL, DD, lp, cmap=plt.cm.bone)
        plt.plot(L, D, 'o', color="#A60628", markersize=12)
        plt.colorbar(c)
        
        ''' plot contours at given chiSq values'''
        for i in range(np.size(level)):
            chiSq[i] = -stats.chi2.ppf(.01*level[i],df = 2)
        chiSq.sort()
        plt.contour(LL, DD, lp, chiSq, hold='on')
        plt.xlabel('$\lambda$', fontsize=20)
        plt.ylabel('$D$',       fontsize=20)  
        plt.show()
        
        return

    def plotPath(self):
        '''plot sample path as a time series'''
        t = np.arange(0, dt*N, dt)
        plt.plot(t, self.x)
