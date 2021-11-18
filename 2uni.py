import matplotlib.pyplot as plt
from numpy import *

def e1():
    # 2x - 3y + 2z = 15
    r = range(-10,10)
    x,y = meshgrid(r,r)

    z = (15 - 2*x + 3*y)/2
    return x, y, z

def e2():
    #A(S) = x**2 + y**2 + z**2 = 4
    a = lambda a: linspace(0,a,100)
    t,p = meshgrid( a(2*pi), a(pi) )
    x = 2*sin(p)*cos(t)
    y = 2*sin(p)*sin(t)
    z = 2*cos(p)

    return x,y,z

def e3():
    # z = x + y^2
    r = linspace(0,1, 1000)
    x,y = meshgrid(r,r)
    z = x + y**2

    return x,y,z

def e27():
    # z = y^.5
    x,z = meshgrid(linspace(0,5,100), linspace(-3,3,100))
    y = (9 - z**2)**.5

    return x,y,z

def e28():
    t, p = meshgrid( linspace(0,3*pi/2,1000), linspace(0,5*pi/6,1000) )
    x = sin(p)*cos(t)
    y = sin(p)*sin(t)
    z = -cos(p)

    return x,y,z

def cone():
    z,t = meshgrid( linspace(0,10,100), linspace(0, 2*pi, 100) )
    y = z*sin(t)
    x = z*cos(t)

    return x,y,z

def paraboloide_hiperbolico():
    z,t = meshgrid( linspace(0,10,100), linspace(0, 2*pi, 100) )
    y = z*sin(t)
    x = z*cos(t)

    return x,y,z**2

def p(*v):
    if(len(v[0]) == 2):
        fig = plt.figure(111) 
        ax = fig.add_subplot()
        ax.set_aspect(1./ax.get_data_ratio())
        
        ax.spines['left'].set_position("zero")
        ax.spines['bottom'].set_position("zero")
        ax.spines['right'].set_color("none")
        ax.spines['top'].set_color("none")

        plt.plot(v[0][0], v[0][1])
    else:
        axis = plt.figure().add_subplot(projection='3d')
        axis.plot_surface(v[0][0], v[0][1], v[0][2])

    plt.show()

def main():
    #p(e1())
    #p(e2())
    p(paraboloide_hiperbolico())
    #p(e3())
    #p(e27())
    #p(e28())
    #p(cone())

main()
