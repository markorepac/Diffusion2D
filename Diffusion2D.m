clear all, close all, clc

% Physics
Lx = 10; % size of model in x, m
Ly = 10; % size of model in y, m
Dc = 1; % Diffusion coefficient, m^2/s
tt = 1; % total time, s
C0 = 1; % amplitude of inital concentration
wx = 0.1 * Lx; % width of gaussian concentration
wy = 0.1 * Ly; % wifth of gaussian concentration in y
cx = 0;
cy = 0; % centers of gaussian inital distribution

% numerics
nx = 50; % number of grid points in x
ny = 50; % number of grid points in y

% preprocessing
dx = Lx/(nx-1); % grid spacing in x, m
dy = Ly/(ny-1); % grid spacing in y, m
dt = min(dx,dy)^2/(Dc)/4; % time interval based on numerical stability, s
%dt = 1e-3; % time interval for playing, s
[X Y] = ndgrid(-Lx/2:dx:Lx/2, -Ly/2:dy:Ly/2);
nt =tt/dt;

% Initial conditions
C = C0 * exp(-(X - cx).^2/wx^2 -(Y - cy).^2/wy^2);
time = 0;
% Action
for it = 1:nt
    dCdt = Dc * (diff(diff(C(:,2:end-1),1,1)/dx,1,1)/dx + diff(diff(C(2:end-1,:),1,2)/dy,1,2)/dy);
    C(2:end-1,2:end-1) = C(2:end-1,2:end-1) + dCdt * dt;
    time = time + dt;

    %postproccesing
    contourf(X,Y,C), shading interp
    colorbar   
    title(['2D diffusion after ', num2str(time), ' sec' ])
    drawnow
end