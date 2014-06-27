# Estimating approximate likelihood inference for the parameters of the one dimensional drift-diffusion process:
# This work is under progress:
#
{
 "metadata": {
  "name": "drift"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "import numpy as np\nimport matplotlib as mpl\nimport matplotlib.pyplot as plt\nimport pylab as pl\nfrom __future__ import division",
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "The one dimensional drift-diffusion process is described by the following stochastic differential equation:\n$dx = adt + \\sqrt{2D}dW$ for which the Fokker-Planck equation is $\\frac{\\partial P}{\\partial t}  = D \\frac{\\partial^{2}P}{\\partial x^{2}}\n-a\\frac{\\partial P}{\\partial x}$. a is a drift and W is a wiener process which models white noise. The transition probability density is\ngiven by $P(x,t) = \\frac{1}{\\sqrt{2\\pi Dt}}\\exp{-\\frac{(x-at)^{2}}{2Dt}}$. The exact solution is the Gaussian with mean and variance given\nby $\\langle x(t)\\rangle = \\int\\limits_{-\\infty}^\\infty x p(x,t)dx$ = at, $\\langle x^{2} \\rangle - \\langle x \\rangle ^2$ = Dt so that the\ntransition probability density is given by $P(x,t) = \\frac{1}{\\sqrt{2\\pi Dt}}\\exp{-\\frac{(x-at)^{2}}{2Dt}}$.\nThe parameters are $a = \\frac{\\langle x(t)\\rangle}{t}$, $ D = \\frac{\\langle x^{2} \\rangle - \\langle x \\rangle ^2}{t}$. The parameter in this \nprocess is  D and a.\n",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "The one dimensional drift-diffusion process and its transition probability density",
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 5
    }
   ],
   "metadata": {}
  }
 ]
}
