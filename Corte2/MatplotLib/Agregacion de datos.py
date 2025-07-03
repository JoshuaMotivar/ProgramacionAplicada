import matplotlib.pyplot as plt
import numpy as np


x_huge = np.linspace(0, 100, 10000)
y_huge = np.sin(x_huge) + np.random.normal(0, 0.1, size=x_huge.shape)


bins = np.linspace(0, 100, 100)
y_aggregated = [np.mean(y_huge[(x_huge >= bins[i]) & (x_huge < bins[i+1])]) for i in range(len(bins)-1)]

plt.plot(bins[:-1], y_aggregated)
plt.title("Aggregated Plot")
plt.xlabel("X")
plt.ylabel("Average Y")
plt.show()
