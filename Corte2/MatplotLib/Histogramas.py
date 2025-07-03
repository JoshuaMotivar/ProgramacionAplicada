import matplotlib.pyplot as plt
import numpy as np
ages = np.random.randint(18, 65, size=2000)

plt.hist(ages, bins=10, color='purple', edgecolor='black')
plt.title("Age Distribution of Survey Participants")
plt.xlabel("Age")
plt.ylabel("Number of Participants")
plt.show()
