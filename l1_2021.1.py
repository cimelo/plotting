import matplotlib.pyplot as plt
from numpy import *

def c():
    t = linspace(0, 2*pi, 1000)
    x = 2*cos(t)
    y = 2*sin(t)
    z = x**2
    return x, y, z

def c2():
    x = linspace(-2, 2, 1000)
    y = sqrt(4-x**2)
    z = x**2
    return x,y,z

def q3():
    t = linspace(-2*pi, 2*pi, 1000)
    x = cos(t)*e**(t)
    y = sin(t)*e**(t)
    return x, y, t

def main():
    fig = plt.figure(111) 
    ax = fig.add_subplot(projection='3d')

    """
    x,y,z = c()
    plt.plot(x, y, z)
    x,y,z = c2()
    plt.plot(x, y, z)
    """

    """
    q3
    ax = fig.add_subplot()
    ax.set_aspect(1./ax.get_data_ratio())
    
    ax.spines['left'].set_position("zero")
    ax.spines['bottom'].set_position("zero")
    ax.spines['right'].set_color("none")
    ax.spines['top'].set_color("none")
    """
    
    x,y,z = q3()
    plt.plot(x,y,z)
    
    plt.show()

if __name__ == '__main__':
    main()
