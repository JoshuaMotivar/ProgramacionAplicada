import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1,13)
sales = np.random.randint(2000, 4000, size=len(months))
plt.plot(months, sales, color='red', linestyle='--', marker='o')
plt.title("Monthly Sales of Product ")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.grid(True)
plt.show()
