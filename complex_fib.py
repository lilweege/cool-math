'''
Luigi Quattrociocchi
April 23 2021
Complex fibonacci 'sequence'
https://www.youtube.com/watch?v=ghxQA3vvhsk
https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
'''

from cmath import sqrt
from math import ceil
import matplotlib.pyplot as plt

def binet(n):
    '''
    https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
    
    Args:
        n (int, float)
    Returns:
        F_n (complex)
    '''
    
    F_n = (1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n
    F_n /= pow(2, n) * sqrt(5)
	
    if not isinstance(F_n, complex):
        F_n = complex(F_n)
    return F_n.real, F_n.imag




# yeah this is not ideal but idc
RANGE = (-4, 5)
STEP = 0.02

neg = []
pos = []

x = RANGE[0]
while x <= RANGE[1]:
    (neg if x < 0 else pos).append(binet(x))
    x += STEP

plt.plot(*zip(*neg), color="C1")
plt.plot(*zip(*pos), color="C0")
# also not ideal
plt.scatter(*zip(*(binet(x) for x in range(RANGE[0], 0    ))), color="C1")
plt.scatter(*zip(*(binet(x) for x in range(0, RANGE[1] + 1))), color="C0")
plt.show()

