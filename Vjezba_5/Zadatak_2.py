import calculus as clc
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

a, b = 0, 3
n_vrijednosti = [5, 10, 50]
analitika = (b**3 - a**3) / 3

x = np.linspace(a, b, 300)
y = f(x)
plt.plot(x, y, label='Analitičko rješenje', color='black')

for n in n_vrijednosti:
    dolje, gore = numericka_integracija(f, a, b, n)
    trapez = trapezna_integracija(f, a, b, n)
    plt.axhline(y=dolje, linestyle='--', label=f'Pravokutna donja suma (n={n})')
    plt.axhline(y=gore, linestyle='--', label=f'Pravokutna gornja suma (n={n})')
    plt.axhline(y=trapez, linestyle=':', label=f'Trapezoidna suma (n={n})')

plt.axhline(y=analitika, color='green', linestyle='-', label='Točna vrijednost')
plt.title('Numerička i analitička integracija')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()