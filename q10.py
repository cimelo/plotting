import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 100)

fig = plt.figure() 
ax = fig.add_subplot()
fig.add_subplot(projection="3d")

ax.spines['left'].set_position("zero")
ax.spines['bottom'].set_position("zero")
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")

plt.plot( t*2**.5, np.power(np.e, t), np.power(np.e, -t) )
plt.show()
