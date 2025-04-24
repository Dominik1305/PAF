import Particle as pr
import numpy as np
import matplotlib.pyplot as plt

p1=pr.Particle(10, 40)
dt = np.linspace(0.001, 2, 200)
dometi = np.zeros((len(dt)))

for i in range(len(dt)):
    p1.kosi_hitac(0, 0, dt[i])
    dometi[i]=p1.domet
D_an = (p1.v0**2/9.81)*math.sin(2*math.radians(p1.alfa))
Err = 100*(D_an-dometi)/D_an

plt.figure(figsize=(10,10))
plt.plot(dt, abs(Err))
plt.xlabel('dt[s]')
plt.ylabel('Err[%]')
plt.yscale('log')
plt.show