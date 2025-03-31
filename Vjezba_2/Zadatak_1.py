import numpy as np
import matplotlib.pyplot as plt
def kinematika(F, m, t):
    lista_brzina = []
    lista_put = []
    lista_akceleracija = []
    lista_vrijeme = []
    for i in range (0, t+1):
        a = F/m
        v = a*i
        x=v*i
        lista_akceleracija.append(a)
        lista_brzina.append(v)
        lista_put.append(x)
        lista_vrijeme.append(i)
    print(lista_brzina)
    print(lista_put)
    figure, (a1, a2, a3) = plt.subplots(3, 1)
    a1.plot(lista_vrijeme, lista_akceleracija)
    a1.set_title('a-t graf')
    a2.plot(lista_vrijeme, lista_brzina)
    a2.set_title('v-t graf')
    a3.plot(lista_vrijeme, lista_put)
    a3.set_title('x-t graf')
    plt.show()
kinematika(150, 15, 10)




   

