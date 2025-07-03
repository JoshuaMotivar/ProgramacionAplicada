import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Plot")
plt.show()


plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Z value')
plt.title("2D Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
