import numpy as np
import matplotlib.pyplot as plt

#Physics
Lx = 10 # size of model in x, m
Ly = 10 # size of model in y, m
Dc = 1 # Diffusion coefficient, m^2/s
tt = 1 # total time, s
C0 = 1 # amplitude of inital concentration
wx = 0.1 * Lx # width of gaussian concentration
wy = 0.1 * Ly # wifth of gaussian concentration in y
cx = 0
cy = 0 # centers of gaussian inital distribution

# numerics
nx = 50  #number of grid points in x
ny = 50  #number of grid points in y

#% Preprocessing
dx = Lx/(nx-1) # grid spacing in x, m
dy = Ly/(ny-1) # grid spacing in y, m
dt = min(dx,dy)**2/(Dc)/4 # time interval based on numerical stability, s
# dt = 1e-3 # time interval for playing, s
x = np.arange(-Lx/2, Lx/2, dx)
y = np.arange(-Ly/2, Ly/2, dy)
X = np.array([[i for i in x] for i in y])
Y = np.array([[j for i in x] for j in y])
nt =round(tt/dt)
#% Initial conditions
C = C0 * np.exp(-(X - cx)**2/wx**2 -(Y - cy)**2/wy**2)
time = 0

# Action
fig, ax = plt.subplots()
plt.ylim(0, 1)
for it in range(nt):
    dCdt = Dc * (np.diff(np.diff(C[:,1:-1],1,0)/dx,1,0)/dx + np.diff(np.diff(C[1:-1,:],1,1)/dy,1,1)/dy)
    C[1:-1,1:-1] = C[1:-1,1:-1] + dCdt * dt
    time = time + dt
    #%postprocessing
           
    plt.cla()
    #plt.ylim(0, 1)           
    ax.pcolor(C)
    plt.pause(0.1)
       

plt.show()