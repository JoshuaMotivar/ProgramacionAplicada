import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)
plt.violinplot(data)
plt.title("Violin Plot")
plt.ylabel("Values")
plt.show()
