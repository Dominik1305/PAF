import numpy as np

class HarmonicOscillator:
    def __init__(self, masa, k, x0, v0):
        self.m = masa          # masa
        self.k = k             # konstanta sile
        self.x0 = x0           # početni položaj
        self.v0 = v0           # početna brzina
        self.omega = np.sqrt(k / masa)  # početna frekvencija

    def analiticko_rjesenje(self, t):
        A = self.x0
        B = self.v0 / self.omega
        x = A * np.cos(self.omega * t) + B * np.sin(self.omega * t)
        v = -A * self.omega * np.sin(self.omega * t) + B * self.omega * np.cos(self.omega * t)
        a = -self.omega**2 * x
        return x, v, a

    def euler_method(self, dt, T):
        N = int(T / dt)
        t = np.linspace(0, T, N)
        x = np.zeros(N)
        v = np.zeros(N)
        a = np.zeros(N)

        x[0] = self.x0
        v[0] = self.v0
        a[0] = -self.k / self.m * x[0]

        for i in range(1, N):
            a[i - 1] = -self.k / self.m * x[i - 1]
            x[i] = x[i - 1] + v[i - 1] * dt
            v[i] = v[i - 1] + a[i - 1] * dt
            a[i] = -self.k / self.m * x[i]

        return t, x, v, a