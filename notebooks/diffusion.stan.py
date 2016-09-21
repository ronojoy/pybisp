# -*- coding: utf-8 -*-
diffusion_code = """
data {
    int<lower=0> n;    // number of data points
    real<lower=0> dt;  // sampling interval  
    real x[n];         // positions 
}
transformed data {
    real dx[n-1];      // displacements
    for (i in 1:n-1)
        dx[i] <- x[i+1] - x[i];
}
parameters {
    real<lower=0> D;  // diffusion coefficient 
}
transformed parameters {
    real<lower=0>sigma; 
    sigma <- sqrt(2*D*dt); 
}
model {
    dx ~ normal(0, sigma);
}
generated quantities {}
"""
