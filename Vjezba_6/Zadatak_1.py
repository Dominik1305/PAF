import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscilator import HarmonicOscillator

m = 1.0         # kg
k = 1.0         # N/m
x0 = 1.0        # m
v0 = 0.0        # m/s
T = 10          # ukupno vrijeme simulacije
osc = HarmonicOscillator(m, k, x0, v0)

for dt in [0.1, 0.01, 0.001]:
    t, x_num, v_num, a_num = osc.euler_method(dt, T)
    x_ana, v_ana, a_ana = osc.analiticko_rjesenje(t)

    error_x = np.abs(x_ana - x_num)

    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, x_num, label='Numeričko', linestyle='--')
    plt.plot(t, x_ana, label='Analitičko', alpha=0.6)
    plt.title(f"x - t (dt = {dt})")
    plt.ylabel("Položaj x (m)")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, v_num, '--', label='Numeričko')
    plt.plot(t, v_ana, label='Analitičko', alpha=0.6)
    plt.ylabel("Brzina v (m/s)")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, a_num, '--', label='Numeričko')
    plt.plot(t, a_ana, label='Analitičko', alpha=0.6)
    plt.xlabel("Vrijeme t (s)")
    plt.ylabel("Ubrzanje a (m/s²)")
    plt.legend()
    plt.show()
    print(f"Max |pogreška položaja| za dt = {dt:.4f}: {np.max(error_x):.6f}")
    

