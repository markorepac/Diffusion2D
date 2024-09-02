# Diffusion2D

Simple 2D diffusion code solving it numerically using finite differences method

Solving for 2D diffusion equation 

$$\frac{\partial{C}}{\partial{t}} = D\left(\frac{\partial^2{C}}{\partial{x^2}} + \frac{\partial^2{C}}{\partial{y^2}}\right) $$

This applies to all diffusion-like problems like heat diffusion where we would have Temperature instead of C.

$$\frac{\partial{T}}{\partial{t}} = D\left(\frac{\partial^2{T}}{\partial{x^2}} + \frac{\partial^2{T}}{\partial{y^2}}\right) $$

where D is in that case thermal diffusivity kappa

$$ D = \kappa = \frac{k}{\rho C_p} $$

The file Diffusion2D.m is MATLAB code that simulates consecutive timestep evaluations of concentration from initial conditions.
The initial concentration distribution is set to be Gaussian distribution centered around x=0, y=0. Below is a contour plot animation


https://github.com/user-attachments/assets/5461f882-6e59-4c3e-9aa0-b232094a740a


Diffusion2D.py is the Python file that makes the same simulation from the same equation. The video of the Python version is below

![Diffusion2D](https://github.com/user-attachments/assets/5af9cd6d-6ec7-4fb9-8379-3934bc017272)

