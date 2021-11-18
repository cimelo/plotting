#!/usr/bin/python

import matplotlib.pyplot as plt
from numpy import *

# Graphs
def trocloide(d, r, t):
    x = t*r - d*sin(t)
    y = r - d*cos(t)
    return x, y

def elipse(a, b, t):
    x = cos(t)*a**2
    y = sin(t)*b**2
    return x, y


t = linspace(0, 100, 1000)
t1 = linspace(0, 2*pi, 1000)
t2 = linspace(-3, 3, 1000)

fig = plt.figure(111) 
ax = fig.add_subplot()
ax.set_aspect(1./ax.get_data_ratio())

ax.spines['left'].set_position("zero")
ax.spines['bottom'].set_position("zero")
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")

"""
plt.plot( t**2-2*t, t**.5)
plt.plot( sin(2*t1), sin(t1+sin(2*t1)) )
plt.plot( cos(5*t1), sin(2*t1) )
plt.plot( t+sin(4*t1), t**2+cos(3*t1) )
plt.plot( sin(2*t1)/(4+t**2), cos(2*t1)/(4+t**2) )
plt.plot( t2-3*t2**2+t2**5, t2 )
plt.plot( 2*sin(t1), 1+2*cos(t1) )
plt.plot( 2*cos(t1/2 + pi/2), 1+2*sin(t1/2+pi/2) )
x = [ 2+2*cos(t1), 2+cos(pi+t1/2), 1+.25*cos(t1), 3+.25*cos(t1) ]
y = [ 2+2*sin(t1), 2+sin(pi+t1/2),  3+.25*sin(t1), 3+.25*sin(t1) ]
for i in range(0,4):
    plt.plot(x[i],y[i])
a = t1*2/3+5*pi/6
x = [ 1+t1*0, 10+t1*0, 3+cos(a), 8+cos(a), 10+t1, 1+t1*9/(2*pi) ]
b = 4-2.5*t1/(2*pi)
y = [ b, b, 1+sin(a), 1+sin(a), 4+t1, 1.5+t1*0 ]
for i in range(0,6):
    plt.plot(x[i],y[i])
"""

x, y = trocloide(1.5, 1, t1*2)
plt.plot(x, y)

plt.show()
