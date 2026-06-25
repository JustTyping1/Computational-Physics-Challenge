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
e = 1.602176634e-19
c = 299792458

wavelength = np.linspace(100, 2000, 1000) * 1e-9 

metal = "lead"

def stopping_voltage(metal):
    wf = work_function[metal]
    V = (h*c)/(wavelength*e) - wf
    return np.maximum(0, V)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3)

line, = ax.plot(
    wavelength * 1e9,
    stopping_voltage(metal)
)

ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Stopping Voltage (V)")
ax.set_title(f"Wavelength of incedent light vs stopping voltage for ({metal})")
ax.grid()

radio_ax = plt.axes([0.05, 0.3, 0.15, 0.4])
radio = RadioButtons(radio_ax, list(work_function.keys()))

def update(label):
    line.set_ydata(stopping_voltage(label))
    ax.set_title(f"Wavelength of incedent light vs stopping voltage for ({label})")
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

radio.on_clicked(update)

plt.show()