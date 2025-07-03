import matplotlib.pyplot as plt
import numpy as np
groupings = ['Musical Instruments', 'Furniture', 'Clothing', 'Food']
revenue = [50000, 30000, 20000, 40000]

plt.bar(groupings, revenue, color='green')
plt.title("Revenue by Product Grouping")
plt.xlabel("Group")
plt.ylabel("Revenue (EURO)")
plt.show()
