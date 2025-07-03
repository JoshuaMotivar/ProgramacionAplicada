import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()
