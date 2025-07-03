import matplotlib.pyplot as plt
import numpy as np
companies = ['Company W', 'Company X', 'Company Y', 'Company Z']
market_share = [40, 30, 20, 10]

plt.pie(market_share, labels=companies, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red'])
plt.title("Market Share by Company")
plt.show()
