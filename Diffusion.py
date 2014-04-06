import numpy as np
from scipy.sparse import spdiags,linalg,eye
import matplotlib.pyplot as plt

#Initialise the parameter values:
D = 2.8
dh, dt = 1.0, 1e-3
m, T = 150, 2000

class diffusion():
    '''
    Class to solve a PDE
    '''
    # Function inside a class:
    def f(self, p):
        return p

        
    def laplacian(self, m):
        """Construct a sparse matrix that applies the 5-point laplacian discretization:"""
        e=np.ones(m**2)
        e2=([1]*(m-1)+[0])*m
        e3=([0]+[1]*(m-1))*m
        h=dh
        A=spdiags([-4*e,e2,e3,e,e],[0,-1,1,-m,m],m**2,m**2)
        A/=h**2
        return A
        
        
        def integrate(self, L, x,y, p):
        '''
        It will do the integration and
        plots it at first and last instant
        '''
        t = 0
        
         for i in range(T):
            
            p = p - dt*(self.f(p)-D*L.dot(p))
        
            if i==0 or i==T-2:
                p1=p.reshape((m,m))
                plt.ion()
                plt.pcolormesh(x,y,p1,shading='gouraud')
                plt.axis('image')
                plt.title(str(i))
                plt.show()
                plt.clf()
                
 rm = diffusion() # instantiate the class

# generate the grid and initialise the field
x = np.linspace(-1,1,m)
y = np.linspace(-1,1,m)
X,Y = np.meshgrid(x,y)


# Initial data
p1=np.random.randn(m*m, 1);

# construct the laplacian
L = rm.laplacian(m)

# Integrate
rm.integrate(L,x,y,p1)
