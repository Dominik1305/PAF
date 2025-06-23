# Koristeći razvijenu klasu iz Vježbi 7 ispitajte kako domet projektila ovisi o koeficijentu trenja CD, a kako o
# masi čestice. U oba slučaja fiksirajte vrijednosti svih ostalih parametara. Koristite razumne fizikalne velicine
# i Runge-Kutta metodu.

import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, kut_alfa, v0, masa, Cd, A=0.01, rho=1.225, g=9.81):
        self.kut_alfa = np.radians(kut_alfa)
        self.v0 = v0
        self.vx = v0 * np.cos(self.kut_alfa)
        self.vy = v0 * np.sin(self.kut_alfa)
        self.masa = masa
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.g = g

    def derivacije(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        Fd = 0.5 * self.Cd * self.rho * self.A * v**2
        Fdx = -Fd * (vx / v)
        Fdy = -Fd * (vy / v)
        Fgx = 0
        Fgy = -self.masa * self.g
        ax = (Fdx + Fgx) / self.masa
        ay = (Fdy + Fgy) / self.masa
        return ax, ay

    def runge_kutta(self, dt=0.01):
        x, y = 0, 0
        vx = self.v0 * np.cos(self.kut_alfa)
        vy = self.v0 * np.sin(self.kut_alfa)
        x_lista = [x]
        y_lista = [y]
        
        while y >= 0:
            ax1, ay1 = self.derivacije(vx, vy)
            k1vx = ax1 * dt
            k1vy = ay1 * dt
            k1x = vx * dt
            k1y = vy * dt

            ax2, ay2 = self.derivacije(vx + 0.5 * k1vx, vy + 0.5 * k1vy)
            k2vx = ax2 * dt
            k2vy = ay2 * dt
            k2x = (vx + 0.5 * k1vx) * dt
            k2y = (vy + 0.5 * k1vy) * dt

            ax3, ay3 = self.derivacije(vx + 0.5 * k2vx, vy + 0.5 * k2vy)
            k3vx = ax3 * dt
            k3vy = ay3 * dt
            k3x = (vx + 0.5 * k2vx) * dt
            k3y = (vy + 0.5 * k2vy) * dt

            ax4, ay4 = self.derivacije(vx + k3vx, vy + k3vy)
            k4vx = ax4 * dt
            k4vy = ay4 * dt
            k4x = (vx + k3vx) * dt
            k4y = (vy + k3vy) * dt

            vx += (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6
            vy += (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6
            x += (k1x + 2 * k2x + 2 * k3x + k4x) / 6
            y += (k1y + 2 * k2y + 2 * k3y + k4y) / 6

            x_lista.append(x)
            y_lista.append(y)

        return x_lista, y_lista

    def get_range(self):
        x_lista, _ = self.runge_kutta()
        return x_lista[-1]

masa = 0.5
Cd_vrijednosti = np.linspace(0.1, 1.0, 10)
lista_cd = []

for Cd in Cd_vrijednosti:
    p = Projectile(v0=50, kut_alfa=45, masa=masa, Cd=Cd)
    lista_cd.append(p.get_range())

plt.figure(figsize=(10, 5))
plt.plot(Cd_vrijednosti, lista_cd, marker='o')
plt.xlabel("Koeficijent otpora Cd")
plt.ylabel("Domet (m)")
plt.title("Ovisnost dometa o koeficijentu otpora Cd")
plt.grid()
plt.show()

Cd = 0.7
masa_vrijednosti = np.linspace(0.05, 1.0, 10)
lista_masa = []

for masa in masa_vrijednosti:
    p = Projectile(v0=50, kut_alfa=45, masa=masa, Cd=Cd)
    lista_masa.append(p.get_range())

plt.figure(figsize=(10, 5))
plt.plot(masa_vrijednosti, lista_masa, marker='o', color='orange')
plt.xlabel("Masa projektila (kg)")
plt.ylabel("Domet (m)")
plt.title("Ovisnost dometa o masi projektila")
plt.grid()
plt.show()
    

    





             

        




    





    


    
    
      
    

    


         
    
    


