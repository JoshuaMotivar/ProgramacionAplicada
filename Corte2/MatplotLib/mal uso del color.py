import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, color='red', label='sin(x)')
plt.plot(x, y2, color='green', label='cos(x)')
plt.title("Plot with Non-Colorblind-Friendly Colors")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


plt.plot(x, y1, color='#0072B2', label='sin(x)') 
plt.plot(x, y2, color='#D55E00', label='cos(x)')  
plt.title("Plot with Colorblind-Friendly Colors")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
