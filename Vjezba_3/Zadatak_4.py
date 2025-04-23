import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 100)
y = 5*x + np.random.normal(loc = 0, scale=25)
a = np.linspace(3.5, 6.5, 5)
pravci = np.zeros((len(x), len(a)))
suma = np.zeros(len(a))

for i in range(len(a)):
    pravci[:, i]=x*a[i]
    suma[i] = sum((y-pravci[:,i])**2)

indeks=suma.indeks(min(suma))
plt.figure()
plt.scatter(x, y)
plt.plot(x, pravci, 'k')
plt.show()


