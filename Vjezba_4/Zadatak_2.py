import math
import matplotlib.pyplot as plt

class Projektil:
    def __init__(self, v0, theta_deg, g=9.81):
        self.v0 = v0
        self.theta = math.radians(theta_deg)
        self.g = g
        self.v0x = v0 * math.cos(self.theta)
        self.v0y = v0 * math.sin(self.theta)
    
     def range(self):
        return (self.v0 ** 2) * math.sin(2 * self.theta) / self.g

     def time(self):
        return 2 * self.v0y / self.g
    

class Numeric_simulate:
    def __init__(self, projektil):
        self.projektil = projektil

    def simulate_range(self, dt):
        x, y = 0.0, 0.0
        vx = self.projektil.v0x
        vy = self.projectile.v0y
        g = self.projectile.g

        while y >= 0:
            x += vx * dt
            y += vy * dt
            vy -= g * dt

        return x
    

class Pogreska:
    def __init__(self, projektil, simulator):
        self.projektil = projektil
        self.simulator = simulator
        self.exact_range = projektil.pogreska()

    def relativna_pogreska(self, dt):
        numerical_range = self.simulator.simulate_range(dt)
        return abs(numerical_range - self.exact_range) / self.exact_range

    def analiza_pogresaka(self, dt_vrijednosti):
        rezultati = []
        for dt in dt_rezultati:
            greska = self.relativna_pogreska(dt)
            rezultati.append((dt, greska))
        return rezultati
    
v0 = 10
theta = 60
projektil = Projektil(v0, theta)
simulator = NUmeric_simulate(projektil)
analiza = Analiza_pogresaka(projektil, simulator)
dt_values = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1]
greske = analiza.analiza_pogresaka(dt_values)

for dt, gr in greske:
    print(f"∆t = {dt:.3f} s -> relativna pogreška = {gr:.5f}")