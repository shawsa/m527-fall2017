from scipy.special import jv
import numpy as np
import matplotlib.pyplot as plt

def p4_helper(C1, C2):
    x = np.linspace(-10,10, 1000)
    y = C1*jv(1.0/3, np.exp(-1*x)) + C2*jv(-1.0/3, np.exp(-1*x))
    plt.plot([0,0], [-10,10], 'k-')
    plt.plot([-10,10], [0,0], 'k-')
    plt.plot(x,y,'b-')
    plt.xlim(-5,5)
    plt.ylim(-1.1, 1.1)
    plt.show()
    
def p4():
    p4_helper(1,0)
    p4_helper(0,1)
    p4_helper(1,1)
    p4_helper(.5,.3)
