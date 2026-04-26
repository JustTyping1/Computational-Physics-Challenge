import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# constants
h = 6.62607015e-34
c = 299792458
k = 1.380649e-23

# blackbody spectrum
def spectrum(wavelength_nm, T):
    lam = wavelength_nm * 1e-9   # nm -> m
    z = h*c/(lam*k*T)
    return (2*h*c**2)/(lam**5) / np.expm1(z)

# wavelength axis
x = np.linspace(100, 3000, 1000)

# initial temperature
T0 = 1000
y = spectrum(x, T0)

# make figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# initial plot
[line] = ax.plot(x, y, lw=2)

ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Intensity")
ax.set_title("Blackbody Radiation")

# slider axis: [left, bottom, width, height]
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])

temp_slider = Slider(
    ax=slider_ax,
    label='Temperature (K)',
    valmin=500,
    valmax=10000,
    valinit=T0
)

# update function
def update(val):
    T = temp_slider.val
    y = spectrum(x, T)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

temp_slider.on_changed(update)

plt.show()