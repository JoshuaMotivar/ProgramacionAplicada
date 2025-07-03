import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)


fig, ax = plt.subplots()
line, = ax.plot(x, y)
ax.set_ylim(-1.5, 1.5)  


def update(frame):
    line.set_ydata(np.cos(x + frame / 10))  
    return line,


ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True)


plt.show()
