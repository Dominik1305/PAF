import numpy as np
import math 
import matplotlib.pyplot as plt

x=[12.5, 3.2, 4, 58.457, 654, 89, 1356, 45.4675, 9.42]
sum_x = 0
for i in x:
    sum_x = sum_x +1

avg_x = sum_x/len(x)

sigma_x = 0
for i in x:
    sigma_x+=(i-avg_x)**2

sigma_x=math.sqrt(sigma_x/len(x))

plt.figure()
plt.plot(x, marker='o', markersize=5, c='k', label='Podatci')
plt.axhline(avg_x, c='r', label=avg_x)
plt.axhline(avg_x+sigma_x, c='b', label=sigma_x)
plt.axhline(avg_x-sigma_x, c='b')
plt.legend()
plt.show()

print(np.mean(x))
print(np.std(x))