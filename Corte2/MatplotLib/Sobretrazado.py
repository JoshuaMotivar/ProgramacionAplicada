import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(10000)
y = np.random.rand(10000)


plt.scatter(x, y)
plt.title("Scatter Plot with Over-plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


plt.scatter(x, y, alpha=0.1)  
plt.title("Scatter Plot with Reduced Over-plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
