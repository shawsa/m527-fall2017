import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save


curve_color = 'b'
curve_size = 3
orientation_size = 15
plt.figure( figsize=(10,10))

def foo(x, y):
    return -y, x

#axies
plt.plot([-10,10], [0,0], 'k-')
plt.plot([0,0], [-10,10], 'k-')


#curve
#t = np.linspace(0, 1, 1000)
th = np.linspace(-np.pi, np.pi, 1000)
xs = 5*np.cos(th)
ys = 5*np.sin(th)

plt.plot(xs, ys, curve_color+'-', linewidth=curve_size)
plt.plot( [5], [0], curve_color+'^', ms=orientation_size)
plt.plot( [-5], [0], curve_color+'v', ms=orientation_size)

plt.xlim( (-8.5, 8.5) )
plt.ylim( (-7.5, 7.5) )

#arrows
for x, y in zip(xs[::50], ys[::50]):
    dx, dy = foo(x,y)
    plt.arrow(x,y,dx,dy, shape='full', lw=2, length_includes_head=True, head_width=.1, color='r')

#plt.savefig('hw5_figure_1.png')
#plt.show()


tikz_save('hw5_figure_1.tex')