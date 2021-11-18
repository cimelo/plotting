import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-2*np.pi, 2*np.pi, 1000)

x = t+2*np.sin(2*t)
y = t+2*np.cos(5*t)

ax = plt.figure().add_subplot()

ax.spines['left'].set_position("zero")
ax.spines['bottom'].set_position("zero")
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")

plt.plot(x, y)
plt.show()
