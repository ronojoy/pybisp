
The Ornstein-Uhlenbeck process obeys the stochastic differential equation

$$ \dot x = -\Gamma x + \xi$$

where $\xi(t)$ is a Gaussian, white noise with zero mean and variance  $ \langle \xi(t)\xi(t^{\prime}) \rangle = 2k_BT\Gamma\delta(t - t^{\prime})$ chosen to ensure that the stationary probability distribution of $x$ is the Gibbs distribution with potential $U(x) = \frac12 kx^2$. Under this constraint, there is only a single parameter in the process, the relaxation rate $\Gamma$. The solution for the sample path is 

$$ x(t) = x(0)e^{-\Gamma t} + \int_0^t e^{\Gamma(s-t)}\xi(s)ds$$

The process mean is  $ \mu(t) = \langle x(t) \rangle = x(0)e^{-\Gamma t} $ and the process variance is $ \sigma^2(t) = \langle (x(t) - \mu(t))^2 \rangle = \frac{k_BT}{k}(1 - e^{-2\Gamma t}) $. Since the noise is a Gaussian process and the stochastic differential equation is linear, $x(t)$ is also a Gaussian process. The mean and the variance, then,  determine the transition probability density uniquely to be

$$P(xt | x't') = \frac{1}{\sqrt{2\pi\sigma^2(\tau)}}e^{-\frac12\frac{(x - \mu(\tau))^2}{\sigma^2(\tau)}}$$

where $ \tau = t - t^{\prime}$ and $\mu(\tau) = x^{\prime} e^{-\Gamma \tau}$.


## Inference 

The inference problem for $\Gamma$ can be stated as follows. Given a discretely sampled path of the process, compute the probability distribution of $\Gamma$. We use Bayes theorem for this and write the probability density of $\Gamma$, given the discrete path samples $\{x_1, x_2, \ldots x_N\}$ as 

$$ P(\Gamma | x_1, x_2, \ldots x_N)  = \frac{\Pi_{i=1}^N P(x_i | x_{i-1}, \Gamma)P(\Gamma)}{\int d\Gamma \Pi_{i=1}^N P(x_i | x_{i-1}, \Gamma)P(\Gamma)}$$

Here, $P(\Gamma)$ is the prior distribution of $\Gamma$ which we shall take to be a flat prior( constant for $\Gamma >0$ and $0$ otherwise) in a pre-defined range or Jeffrey prior. To logarithm of the probability distribution is 

$$ \log P(\Gamma | x_1, x_2, \ldots x_N) = \sum_{i=1}^N \log P(x_i | x_{i-1}, \Gamma) + \log P(\Gamma)  - \log \int d\Gamma \Pi_{i=1}^N P(x_i | x_{i-1}, \Gamma)P(\Gamma) $$

Inserting the form of the Ornstein-Uhlenbeck transition probability, this becomes

$$ \log P(\Gamma | x_1, x_2, \ldots x_N) = -\frac12\sum_{i=1}^N \left[\log (2\pi\sigma^2(\tau_i)) - \frac{(x_i - x_{i-1}e^{\Gamma\tau_i})^2}{\sigma^2(\tau_i)}\right]+ \log P(\Gamma)  - \log \int d\Gamma \Pi_{i=1}^N P(x_i | x_{i-1}, \Gamma)P(\Gamma) $$

The best estimate for $\Gamma$ is given by the condition $\frac{\partial \log P}{\partial \Gamma} = 0$. 

$$\frac{\partial log P}{\partial \Gamma} = -\frac{1}{2}\sum_{i=1}^N\Big[-\frac{\partial}{\partial \Gamma}(\frac{x_{i}^2+x_{i-1}^2e^{2\Gamma\tau_{i}}-2x_{i}x_{i-1}e^{\Gamma\tau_{i}})}{\sigma^2(\tau_{i})} \Big]-\log\Gamma^{-1}=0$$

$$\frac{\partial log P}{\partial \Gamma} = -\frac{1}{2}\sum_{i=1}^N\Big[-{2\tau_{i}e^{\Gamma\tau_{i}}x_{i-1}(x_{i-1}e^{\Gamma\tau_{i}}-x_{i})}\Big]- \frac{1}{\Gamma^{2}}$$


## Code has to be written:

