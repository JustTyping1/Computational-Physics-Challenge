# Importing necessary packages
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

x_values = [0]
y_values = [0]

step = 0.1
k = 1000

ax.set_ylim(-0.1*k*step, 0.1*k*step)
ax.set_xlim()
line, = ax.plot([], [], color="black")


def update(frame):
    angle = 2*np.pi*np.random.random()
    x_values.append(x_values[-1] + step*np.cos(angle))
    y_values.append(y_values[-1] + step*np.sin(angle))

    ax.set_ylim(min(y_values)*1.1, max(y_values)*1.1)
    ax.set_xlim(min(x_values)*1.1, max(x_values)*1.1)

    line.set_data(x_values, y_values)
    return line,

ani = animation.FuncAnimation(fig, update, frames=k, interval=1)

plt.show()