import matplotlib.pyplot as plt
import numpy as np

ad_spend = np.random.randint(50, 1000, size=50)
sales = ad_spend * np.random.uniform(0.8, 1.2, size=50)

plt.scatter(ad_spend, sales, color='blue')
plt.title("Advertisement Spending vs. Sales")
plt.xlabel("Ad Spend (USD)")
plt.ylabel("Sales (Units)")
plt.show()
