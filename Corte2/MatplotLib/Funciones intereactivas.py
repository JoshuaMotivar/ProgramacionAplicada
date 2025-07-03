import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y)

def on_click(event):
    
    print(f"The Coordinates were clicked at: ({event.xdata}, {event.ydata})")

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
