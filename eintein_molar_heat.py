import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np

Tevalues = {
    "lead": 79,
    "gold": 124,
    "silver": 169,
    "copper": 258,
    "aluminium": 321,
    "iron": 352
}

h = 6.62607015e-34
k = 1.380649e-23
Rgas = 8.314

T = np.linspace(0, 3000, 1000)

metal = "lead"

def cv(metal):
    x = Tevalues[metal]/T
    return 3*Rgas*(x**2) * ((np.exp(x))/((np.exp(x)-1)**2))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3)

line, = ax.plot(
    T,
    cv(metal)
)

ax.set_xlabel("Temperature/K")
ax.set_ylabel("Molar heat capacity/Jmol^-1K^-1")
ax.set_title(f"Einstein's Molar Heat capacity against temperature for ({metal})")
ax.grid()

radio_ax = plt.axes([0.05, 0.3, 0.15, 0.4])
radio = RadioButtons(radio_ax, list(Tevalues.keys()))

def update(label):
    line.set_ydata(cv(label))
    ax.set_title(f"Einstein's Molar Heat capacity against temperature for ({label})")
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

radio.on_clicked(update)

plt.show()