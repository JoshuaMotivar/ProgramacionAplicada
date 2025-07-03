import matplotlib.pyplot as plt
import numpy as np


days = np.arange(1, 20)
temperature = np.random.normal(loc=25, scale=5, size=len(days))


plt.plot(days, temperature, marker='o')
plt.title("Daily Temperatures in August")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")


plt.savefig("daily_temperatures_august.png", dpi=300, bbox_inches='tight')
plt.savefig("daily_temperatures_august.pdf", format='pdf', bbox_inches='tight')


plt.show()
