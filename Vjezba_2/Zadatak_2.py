import numpy as np
import matplotlib.pyplot as plt
def hitac(v0, th, t, x0, y0):
    g = 9.81
    lista_x = [x0]
    lista_y = [y0]
    lista_vrijeme = [0]
    v0x = v0*np.cos(th)
    v0y = v0*np.sin(th)
    for i in range (1, t+1):
        if lista_y[-1]>0:
            x = x0 + v0*i
            y = y0 + v0y - 1/2 *g*i**2
            lista_x.append(x)
            lista_y.append(y)
            lista_vrijeme.append(i)
            print(y)
    else:
        print("Palo je na pod")
    print(lista_x)
    print(lista_y)
    print(lista_vrijeme)
    figure, (a1, a2, a3) = plt.subplots(3, 1)
    a1.plot(lista_x, lista_y)
    a1.set_title('x-y graf')
    a2.plot(lista_vrijeme, lista_x)
    a2.set_title('x-t graf')
    a3.plot(lista_vrijeme, lista_y)
    a3.set_title('y-t graf')
    plt.show()
hitac(10, 45, 10, 20, 12)

        