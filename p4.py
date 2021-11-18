import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [3.5, 3.50]
plt.rcParams["figure.autolayout"] = False
#plt.figure().add_subplot(projection='3d')
t = np.arange(0, 2*np.pi, .001)
x = np.cos(t)
y = np.sin(t)

ax = plt.figure().add_subplot(111)
plt.plot(x, y)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


plt.show()
