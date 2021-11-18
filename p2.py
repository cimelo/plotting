import math
import matplotlib.pyplot as plt
import numpy as np

def linear():
    s = .5**.5
    y = np.arange(-s, s, 0.001)
    x = y
    z = (1-2*y**2)**.5
    return x, y, z
    
def polar():
    t = np.arange(0, 2*np.pi, 0.001)
    y = np.cos(t)/math.sqrt(2)
    x = -y
    z = np.sin(t)
    return x, y, z

fig = plt.figure()
fig.add_subplot(projection='3d')
x, y, z = linear()
plt.plot(x, y, z)
x1, y1, z1 = polar()
plt.plot(x1, y1, z1)

plt.show()
