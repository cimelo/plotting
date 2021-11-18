import matplotlib.pyplot as plt
from numpy import *

z = arange(0, 100, 0.001)
x = cos(z)
y = sin(z)

plt.figure().add_subplot(projection='3d')
plt.plot(x, y, z)

plt.show()
