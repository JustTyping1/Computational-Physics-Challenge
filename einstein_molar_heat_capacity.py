import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# constants
Tevalues = {
    "lead": 79,
    "gold": 124,
    "silver": 169,
    "copper": 258,
    "aluminium": 321,
    "iron": 352
}
metal = "lead"

h = 6.62607015e-34
Te = Tevalues[metal]
k = 1.380649e-23
Rgas = 8.314



# blackbody spectrum
def cv(T):
    x = Te/T
    return 3*Rgas*(x**2) * ((np.exp(x))/((np.exp(x)-1)**2))

# wavelength axis
x = np.linspace(100, 3000, 1000)

# initial temperature
T0 = 1000
y = cv(x)

# make figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# initial plot
[line] = ax.plot(x, y, lw=2)

ax.set_xlabel("Temperature/K")
ax.set_ylabel("Molar heat capacity/Jmol^-1K^-1")
ax.set_title("Einstein's Molar Heat capacity against temperature for " + metal)

# slider axis: [left, bottom, width, height]
#slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])

#temp_slider = Slider(
 #   ax=slider_ax,
  #  label='Temperature (K)',
   # valmin=500,
    #valmax=10000,
    #valinit=T0
#)

# update function
#def update(val):
 #   T = temp_slider.val
  #  y = spectrum(x, T)
   # line.set_ydata(y)
    #ax.relim()
    #ax.autoscale_view()
    #fig.canvas.draw_idle()

#temp_slider.on_changed(update)

plt.show()