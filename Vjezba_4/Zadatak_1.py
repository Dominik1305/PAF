import Particle as prt
import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init___(self, v0, x0, fi, y0):
        self.y0 = y0 
        self.v0 = v0
        self.x0 = x0
        self.fi = fi
        self.x = [self.x0]
        self.y = [self.y0]
        self.vx = []
        self.vy = []

    def reset(self):
        self.x = [self.x0]
        self.y = [self.y0]
        self.vx = []
        self.vy = []

    def __move(self, dt):
        self.dt = dt
        self.vy.append(self.v0*np.sin(np.radians(self.fi)))
        self.vx.append(self.v0*np.cos(np.radians(self.fi)))
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)

    def range(self, t, dt):
        for i in np.arange(0, t, dt):
            self.__move(self, dt)
        print("Domet je: ", self.x[-1])
         
    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        x_vals, y_vals = zip(*self.trajectory)
        plt.plot(x_vals, y_vals)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("Putanja projektila")
        plt.grid(True)
        plt.show()

