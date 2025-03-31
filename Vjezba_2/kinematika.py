import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, x0, v0, t,dt):
    lista_t = [0]
    lista_x = [x0]
    lista_v = [v0]
    lista_a = [F/m]
    for i in np.arange (0,t,dt):
        v = lista_v[-1]+lista_a[-1]*dt
        x = lista_x[-1]+lista_v[-1]*dt
        
        lista_x.append(x)
        lista_v.append(v)
        lista_a.append(lista_a[-1])
        lista_t.append(i)
    print(lista_a)
    print(lista_x)
    print(lista_v)
    print(lista_t)
    figure, (a1, a2, a3) = plt.subplots(3, 1)
    a1.plot(lista_t, lista_x)
    a1.set_title('x-t graf')
    a2.plot(lista_t, lista_v)
    a2.set_title('v-t graf')
    a3.plot(lista_t, lista_a)
    a3.set_title('a-t graf')
    plt.show()





import math 


def kosi_hitac(v0, fi,t, dt=0.01):
    g = 9.81
    t = np.arange(0, t, dt)
    v0 = 100
    fi = 60
    vx = [v0*math.cos(math.radians(fi))]
    vy = [v0*math.sin(math.radians(fi))]
    x = [0]
    y = [0]
    ax = 0
    ay = -g
    i=0
    for i in range(len(t)-1):
        if y[-1]>=0:
            vx.append(vx[i]+ax*dt)
            vy.append(vy[i]+ay*dt)
            x.append(x[i]+vx[i]*dt)
            y.append(y[i]+vy[i]*dt)
        

    figure, (a1, a2, a3) = plt.subplots(3, 1)
    a1.plot(t, x)
    a1.set_title('x-t graf')
    a2.plot(t, y)
    a2.set_title('y-t graf')
    a3.plot(x, y)
    a3.set_title('x-y graf')
    
    plt.show()


