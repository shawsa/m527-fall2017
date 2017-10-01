import numpy as np
import matplotlib.pyplot as plt


curve_color = 'b'
curve_size = 3
orientation_size = 15
plt.figure( figsize=(10,10))

def foo(x, y):
    return -y**2, x*y

#axies
plt.plot([-10,10], [0,0], 'k-')
plt.plot([0,0], [-10,10], 'k-')


#curve
t = np.linspace(0, 1, 1000)
th = np.linspace(-np.pi/2, np.pi/2, 1000)
xs = np.append( t*0, np.cos(th))
ys = np.append( 1-2*t, np.sin(th))

plt.plot(xs, ys, curve_color+'-', linewidth=curve_size)
plt.plot( [1], [0], curve_color+'^', ms=orientation_size)
plt.plot( [0], [0], curve_color+'v', ms=orientation_size)

plt.xlim( (-1.1, 1.1) )
plt.ylim( (-1.5, 1.5) )

#arrows
for x, y in zip(xs[::50], ys[::50]):
    dx, dy = foo(x,y)
    plt.arrow(x,y,dx,dy, shape='full', lw=2, length_includes_head=True, head_width=.03, color='r')

plt.show()
