import calculus as clc
import numpy as np
import matplotlib.pyplot as plt
def kubna(x):
    y=x**3
    return y
x_lista = []
for i in np.arange(0, 1, 0.0001):
    x_lista.append(i)
y_lista =[]
for i in x_lista:
    y_lista.append(np.cos(i))
A = clc.derivacija1(np.sin, 0, 1, 0.1)
B = clc.derivacija1( np.sin, 0, 1, 0.01)
plt.plot(x_lista, y_lista)
plt.legend(["0.1 razmak","0.01 razmak","analitička"])
plt.show()