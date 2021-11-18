import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)

fig = plt.figure() 
ax = fig.add_subplot()

ax.spines['left'].set_position("zero")
ax.spines['bottom'].set_position("zero")
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")

plt.plot( 2*np.cos(t), t-np.cos(t) )
plt.show()
