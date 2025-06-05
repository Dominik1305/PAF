import numpy as np
import matplotlib.pyplot as plt

G = 6.67408*10**-11
m_Z = 5.9742*10**24     # masa Zemlje (kg)
m_S = 1.989*10**30      # masa Sunca (kg)
T = 365.242             # jedna godina       

x = 1.48*10**11         # astronomska jedinica
y = 0
vx = 0
vy = 29783 

dt = 60 * 60               # 1 sat u sekundama
n = int((365.242 * 24 * 60 * 60) / dt)

x_lista = []
y_lista = []

for i in range(n):
    r = (x**2 + y**2)**0.5
    ax = -G * m_S * x / r**3
    ay = -G * m_S * y / r**3
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt

    x_lista.append(x)
    y_lista.append(y)

plt.plot(x_lista, y_lista, label='Zemlja')
plt.plot(0, 0, 'yo', label='Sunce')  # Sunce u ishodištu
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Putanja Zemlje oko Sunca (Eulerova metoda)')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()