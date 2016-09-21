[pybisp](http://nbviewer.ipython.org/github/ronojoy/pybisp/tree/master/)
======

A collection of Python tools for performing Bayesian parameter estimation and model selection for stochastic processes. The initial roadmap is to implement exact likelihood estimation for the parameters of the 

* Wiener process
* Ornstein-Uhlenbeck process

and approximate likelihood inference for the parameters of the

* general one-dimensional drift-diffusion process
* general three-dimensional Brownian dynamics process with multiplicative noise

Model selection and change point detection methods will be implemented after the above methods have been implemented. Possible applications are to the analysis of particle trajectories of optically trapped particles or to the motion of proteins and filaments in live tracking of cells, as for example, in the references below :

* [Calibrating optical tweezers with Bayesian inference](https://www.opticsinfobase.org/oe/fulltext.cfm?uri=oe-21-25-31578&id=276088)
* [Bayesian Approach to MSD-Based Analysis of Particle Motion in Live Cells](http://www.cell.com/biophysj/abstract/S0006-3495%2812%2900718-7)
* [Stochastic Elastohydrodynamics of a Microcantilever Oscillating Near a Wall ](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.050801)
* [Daniel Ensign's thesis on single molecule trajectories](http://purl.stanford.edu/gb827kt2324)

A related effort, which replaces specific physical models by abstract families of hidden Markov models in the likelihood, is [Simtk-HMM](https://simtk.org/home/bhmm/).

Contributions and ideas are welcome!

### Use

```python
import pybisp as pb
import pandas as pd
data = pb.ReadDataFrame('samplepath.csv') # read time series data 
ou = pb.ou.Inference(data)                # inference assuming Ornstein-Uhlenbeck process 
theta = ou.mapEstimate()                  # get maximum aposteriori parameter estimate
dtheta = ou.erroBar() 			              # get error bar of the MAP estimate
ou.plotLogProb()  			                  # plot the log posterior around the MAP estimate 
```
