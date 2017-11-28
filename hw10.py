import numpy as np
import matplotlib.pyplot as plt

def p3():
    t = np.linspace(0, 2*np.pi, 1000)

    xs_inner = np.pi*np.cos(t) + (4)
    ys_inner = np.pi*np.sin(t) + (-2)

    xs_outer = 3*np.pi*np.cos(-t) + (4)
    ys_outer = 3*np.pi*np.sin(-t) + (-2)

    plt.plot(xs_inner, ys_inner , 'b--')
    plt.plot(xs_outer, ys_outer , 'b--')

    xs_fill = np.concatenate( (xs_inner,xs_outer) )
    ys_fill = np.concatenate( (ys_inner, ys_outer) )
    plt.fill(xs_fill, ys_fill, 'c')

    plt.plot( (-100, 100), (0,0), 'k-')
    plt.plot( (0,0), (-100, 100), 'k-')
    plt.xlim(-6, 15)
    plt.ylim(-12, 8)
    plt.xlabel('Re')
    plt.ylabel('Im')

    plt.show()
    
def p6():
    t = np.linspace(0, 2*np.pi, 1000)

    xs_inner = .5*np.cos(t) + (.5)
    ys_inner = .5*np.sin(t)

    xs_outer = 100*np.pi*np.cos(-t) + (.5)
    ys_outer = 100*np.pi*np.sin(-t)

    plt.plot(xs_inner, ys_inner , 'b--')
    plt.plot(xs_outer, ys_outer , 'b--')

    xs_fill = np.concatenate( (xs_inner,xs_outer) )
    ys_fill = np.concatenate( (ys_inner, ys_outer) )
    plt.fill(xs_fill, ys_fill, 'c')

    plt.plot( (-100, 100), (0,0), 'k-')
    plt.plot( (0,0), (-100, 100), 'k-')
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plt.xlabel('Re')
    plt.ylabel('Im')

    plt.show()