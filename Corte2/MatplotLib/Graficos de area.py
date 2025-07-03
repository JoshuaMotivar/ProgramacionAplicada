import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 1)
y1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y2 = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])


plt.fill_between(x, y1, color='skyblue', alpha=0.5)
plt.fill_between(x, y2, color='orange', alpha=0.5)
plt.title("Misleading Stacked Area Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.fill_between(x, y1, color='skyblue', alpha=0.5)
plt.fill_between(x, y1 + y2, y1, color='orange', alpha=0.5)
plt.title("Improved Stacked Area Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
