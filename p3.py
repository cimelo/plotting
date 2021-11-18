import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.001)
y = (1-x**2)**.5

plt.plot(x, y)
plt.show()
