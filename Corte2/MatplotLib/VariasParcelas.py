import matplotlib.pyplot as plt
import numpy as np


regions = ['North', 'South', 'East', 'West']


sales_data = np.random.randint(500, 5000, size=(4, 12))


months = np.arange(1, 13)  


fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Monthly Sales by Region')


for i, region in enumerate(regions):
    ax = axs[i // 2, i % 2]
    ax.plot(months, sales_data[i], marker='o')
    ax.set_title(region)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales (Units)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  
plt.show()
