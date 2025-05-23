import numpy as np
import matplotlib.pyplot as plt
import math

def akc(V, q, m, E, B):
    vx = V[0]
    vy = V[1]
    vz = V[2]
    Ex = E[0]
    Ey = E[1]
    Ez = E[2]
    Bx = B[0]
    By = B[1]
    Bz = B[2]

    ax = (q/m)*(Ex+vy*Bz-vz*By)
    ay = (q/m)*(Ey-(vx*Bz-vz*Bx))
    az = (q/m)*(Ez+vx*By-vy*Bx)
    return ax, ay, az

def eksplicitna_step(x, y, z, V, dt, q, m, E, B):
    vx = V[0]
    vy = V[1]
    vz = V[2]

    ax, ay, az=akc(V, q, m, E, B)
    vx_novi=vx + ax*dt
    vy_novi=vy + ay*dt
    vz_novi=vz + az*dt
    x_novi=x + vx*dt
    y_novi=y + vy*dt
    z_novi=z + vz*dt
    return x_novi, y_novi, z_novi, vx_novi, vy_novi, vz_novi

x0=0         #m
y0=0         #m
z0=0         #m
V0=[1,0,0]   #m/s
E=[0,0,1]    #V/m, N/C
B=[0,1,0]    #T
q=1
m=1          #kg

x_eksp=[x0]
y_eksp=[y0]
z_eksp=[z0]
vx_eksp=[V0[0]]
vy_eksp=[V0[1]]
vz_eksp=[V0[2]]

dt = 0.001
vrijeme = 10  #s
t = np.arange(0, vrijeme, dt)

for i in range(len(t)):
    X, Y, Z, VX, VY, VZ=eksplicitna_step(x_eksp[-1], y_eksp[-1], z_eksp[-1], V=[vx_eksp[-1], vy_eksp[-1], vz_eksp[-1]], dt=dt, q=q, m=m, E=E, B=B)
    x_eksp.append(X)
    y_eksp.append(Y)
    z_eksp.append(Z)
    vx_eksp.append(VX)
    vy_eksp.append(VY)
    vz_eksp.append(VZ)

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(x_eksp, y_eksp, z_eksp, 'r')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

