import numpy as np
import matplotlib.pyplot as plt
import math

class Projectile:
    def __init__(self, x0, y0, v0, kut_alfa, masa, Cd, A, rho=1.225, g=9.81):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(kut_alfa))
        self.vy = v0 * np.sin(np.radians(kut_alfa))
        self.masa = masa
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.g = g

    def otpor_zraka(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        Fx = -0.5 * self.rho * self.Cd * self.A * v * vx
        Fy = -0.5 * self.rho * self.Cd * self.A * v * vy
        return Fx, Fy
    
    def simulacija(self, dt):
        x_poz, y_poz = [self.x], [self.y]
        vx, vy = self.vx, self.vy
        x, y = self.x, self.y

        while y>=0:
            Fx, Fy = self.otpor_zraka(vx, vy)
            ax = Fx / self.masa
            ay = Fy / self.masa - self.g
            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt
            x_poz.append(x)
            y_poz.append(y)
        return x_poz, y_poz
    
    def testiraj_korake(self):
        dt_vrijednosti = [0.5, 0.2, 0.1, 0.05, 0.01]
        boje = ['r', 'g', 'b', 'm', 'k']

        for i, dt in enumerate(dt_vrijednosti):
            projektil = Projectile(x0=0, y0=0, v0=50, kut_alfa=45, masa=0.145, Cd=0.47, A=0.0042)
            x, y = projektil.simulacija(dt)
            plt.plot(x, y, boje[i], label=f'dt = {dt}')
        plt.title('Putanja projektila za različite vrijednosti ∆t')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.legend()
        plt.grid()
        plt.show()
projektil = Projectile(x0=0, y0=0, v0=50, kut_alfa=45, masa=0.145, Cd=0.47, A=0.0042)
projektil.testiraj_korake()
    


    