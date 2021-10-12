PyBISP
========
[PyBISP](https://github.com/ronojoy/pybisp) is a pure Python package for **B**ayesian **I**nference of **S**tochastic **P**rocesses. 

Currently it can estimate  the parameters of the 

* Wiener process
* Ornstein-Uhlenbeck process

using exact likelihoods from **discretely** observed sample paths. Possible applications are to the analysis of particle trajectories of optically trapped particles or to the motion of proteins and filaments in live tracking of cells, see [related work](#related) below. 

There is a [roadmap](#roadmap) to include Monte Carlo sampling methods for approximate inference of diffusion processes for which exact likelihoods are not available analytically. 

Contributions and ideas are welcome!

### Install

```
pip install pybisp
```
or

```
git clone https://github.com/ronojoy/pybisp.git
cd pybisp
python setup.py install
```

### Use

```python
import pybisp as pb
import pandas as pd
data = pb.ReadDataFrame('samplepath.csv') # read time series data 
dt = 1                                    # choose some dt to use  
ou = pb.ou.Inference(data,dt)                # inference assuming Ornstein-Uhlenbeck process 
theta = ou.mapEstimate()                  # get maximum aposteriori parameter estimate
dtheta = ou.erroBar() 			           # get error bar of the MAP estimate
ou.plotLogProb()  			               # plot the log posterior around the MAP estimate 
```

A [tutorial notebook](https://github.com/ronojoy/pybisp/blob/master/notebooks/optical-trap.ipynb) demonstrates the
use of the package for estimating the stiffness and diffusion coefficient of an optically trapped particle 

### <a name="roadmap"></a>Roadmap

- Approximate likelihood inference of Markov diffusions using short-time expansions of the propagators
- Monte Carlo sampling methods for multidimensional Markov diffusions
- Applications to correlated Brownian motion 


### <a name="related"></a>Related work

* [Stochastic Elastohydrodynamics of a Microcantilever Oscillating Near a Wall ](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.050801)
* [Bayesian Approach to MSD-Based Analysis of Particle Motion in Live Cells](http://www.cell.com/biophysj/abstract/S0006-3495%2812%2900718-7)
* [Calibrating optical tweezers with Bayesian inference](https://www.opticsinfobase.org/oe/fulltext.cfm?uri=oe-21-25-31578&id=276088)
* [Bayesian statistics and single molecule trajectories](http://purl.stanford.edu/gb827kt2324)
