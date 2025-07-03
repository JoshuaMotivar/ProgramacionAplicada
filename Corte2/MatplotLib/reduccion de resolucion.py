import matplotlib.pyplot as plt
import numpy as np


x_huge = np.linspace(0, 100, 10000)
y_huge = np.sin(x_huge) + np.random.normal(0, 0.1, size=x_huge.shape)


x_downsampled = x_huge[::10]
y_downsampled = y_huge[::10]

plt.plot(x_downsampled, y_downsampled)
plt.title("Downsampled Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
