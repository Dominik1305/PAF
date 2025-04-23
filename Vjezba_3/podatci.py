import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("monthly_in_situ_co2_mlo (1)")
CO2 = data[4]
dates = data[3]

plt.figure()
plt.plot(dates, CO2)
plt.show

a,b = np.polyfit(dates, CO2, 1)
c,d,e = np.polyfit(dates, CO2, 2)
plt.plot(dates, CO2)
plt.plot(dates, dates*a+b, 'r')
plt.plot(dates, c*dates**2+d*dates+e, 'g')