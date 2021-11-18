import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 100)

ax = plt.figure().add_subplot(projection='3d')
plt.plot(t, t**2, t**3)

plt.show()
