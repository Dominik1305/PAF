import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, kut, masa, Cd, A, rho=1.225, g=9.81):
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.kut = kut
        self.masa = masa
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.g = g

    def otp_zraka(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        Fx = -0.5 * self.rho * self.Cd * self.A * v * vx
        Fy = -0.5 * self.rho * self.Cd * self.A * v * vy
        return Fx, Fy

    def eulerova_metoda(self, dt):
        vx = self.v0 * np.cos(np.radians(self.kut))
        vy = self.v0 * np.sin(np.radians(self.kut))
        x, y = self.x0, self.y0

        x_poz, y_poz = [x], [y]

        while y >= 0:
            Fx, Fy = self.otp_zraka(vx, vy)
            ax = Fx / self.masa
            ay = Fy / self.masa - self.g

            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt

            x_poz.append(x)
            y_poz.append(y)

        return x_poz, y_poz

    def runge_kutta(self, dt):
        vx = self.v0 * np.cos(np.radians(self.kut))
        vy = self.v0 * np.sin(np.radians(self.kut))
        x, y = self.x0, self.y0

        x_poz, y_poz = [x], [y]

        def derivacije(vx, vy):
            Fx, Fy = self.otp_zraka(vx, vy)
            ax = Fx / self.masa
            ay = Fy / self.masa - self.g
            return ax, ay

        while y >= 0:
            ax1, ay1 = derivacije(vx, vy)
            k1vx = ax1 * dt
            k1vy = ay1 * dt
            k1x = vx * dt
            k1y = vy * dt

            ax2, ay2 = derivacije(vx + 0.5*k1vx, vy + 0.5*k1vy)
            k2vx = ax2 * dt
            k2vy = ay2 * dt
            k2x = (vx + 0.5*k1vx) * dt
            k2y = (vy + 0.5*k1vy) * dt

            ax3, ay3 = derivacije(vx + 0.5*k2vx, vy + 0.5*k2vy)
            k3vx = ax3 * dt
            k3vy = ay3 * dt
            k3x = (vx + 0.5*k2vx) * dt
            k3y = (vy + 0.5*k2vy) * dt

            ax4, ay4 = derivacije(vx + k3vx, vy + k3vy)
            k4vx = ax4 * dt
            k4vy = ay4 * dt
            k4x = (vx + k3vx) * dt
            k4y = (vy + k3vy) * dt

            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6
            x += (k1x + 2*k2x + 2*k3x + k4x) / 6
            y += (k1y + 2*k2y + 2*k3y + k4y) / 6

            x_poz.append(x)
            y_poz.append(y)

        return x_poz, y_poz
    
projektil = Projectile(x0=0, y0=0, v0=50, kut=45, masa=0.145, Cd=0.47, A=0.0042)
dt = 0.01

x_euler, y_euler = projektil.eulerova_metoda(dt)
x_rk, y_rk = projektil.runge_kutta(dt)

plt.plot(x_euler, y_euler, 'r--', label='Eulerova metoda')
plt.plot(x_rk, y_rk, 'b-', label='Runge-Kutta metoda')
plt.title('Usporedba Eulerove i Runge-Kutta metode (dt = 0.01)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid()
plt.show()
