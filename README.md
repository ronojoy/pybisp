[pybisp](http://nbviewer.ipython.org/github/ronojoy/pybisp/tree/master/)
======

A collection of Python tools for performing Bayesian parameter estimation and model selection for stochastic processes. The initial roadmap is to implement exact likelihood estimation for the parameters of the 

* Wiener process
* Ornstein-Uhlenbeck process

and approximate likelihood inference for the parameters of the

* general one-dimensional drift-diffusion process
* general three-dimensional Brownian dynamics process with multiplicative noise

Model selection and change point detection methods will be implemented after the above methods have been implemented.

Contributions and ideas are welcome!

### Use

```python
import pybisp as pb
data = pb.ReadDataFrame('diffusion.csv') # read diffusion time series data from csv
estimate = pb.WienerInference(data) # estimate parameters assuming a Wiener process
```
