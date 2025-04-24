import numpy as np
class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

p1 = Particle(10, -5)
print("Masa cestice = ", p1.mass)
print("Polozaj cestice = ", p1.x_0)