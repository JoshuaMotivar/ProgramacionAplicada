import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10)
y1 = np.random.randint(50, 100, size=10)
y2 = y1 + np.random.randint(-5, 5, size=10)


plt.plot(x, y1, label='Data 1')
plt.plot(x, y2, label='Data 2')
plt.ylim(90, 100)  
plt.title("Plot with Truncated Y-Axis")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


plt.plot(x, y1, label='Data 1')
plt.plot(x, y2, label='Data 2')
plt.title("Plot with Full Y-Axis")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
