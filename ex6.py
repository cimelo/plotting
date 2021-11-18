import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-3, 3, 100)
fig = plt.figure()

ax = fig.add_subplot()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot( t**4-3*t**2, t )
plt.show()
