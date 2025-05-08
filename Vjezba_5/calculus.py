import numpy as np
import matplotlib.pyplot as plt

def derivacija(f, x, dx, three_step=False):
    if three_step==True:
        der=(f(x+dx)-f(x-dx))/(2*dx)
    else:
        der=(f(x+dx) - f(x))/dx
    return der



def derivacija1(f, x1, x2, dx, three_step=False):
    x_lista = []
    for i in np.arange(x1, x2, dx):
        x_lista.append(i)
    lista = []
    for i in np.arange(x1, x2, dx):
        der1 = derivacija(f, i, dx, three_step)
        lista.append(der1)
    plt.plot(x_lista, lista)
    

def numericka_integracija(f, a, b, n):
    dx = (b - a) / n
    donja_suma = 0
    gornja_suma = 0
    for i in range(n):
        x_lijevo = a + i * dx
        x_desno = a + (i + 1) * dx
        donja_suma += min(f(x_lijevo), f(x_desno)) * dx
        gornja_suma += max(f(x_lijevo), func(x_desno)) * dx
    return donja_suma, gornja_suma

def trapezoidna_integracija(func, a, b, n):
    dx = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * dx)
    return total * dx



