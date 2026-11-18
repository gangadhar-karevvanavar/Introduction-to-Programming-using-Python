#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:11:04 2023

@author: bharath
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:32:55 2023

@author: bharath
"""


class my_tuple(tuple):
    def __init__(self,tup):
        self.tup = tup
        
    def add(self,var):
        lis = list(self.tup)
        lis.append(var)
        tup = tuple(lis)
        return tup
    
tup = (1,2,3)
tup = my_tuple(tup)
# The following should add 4
tup = tup.add(3)
print(tup)


import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3] 
y = [0, 1, 4, 9]
plt.plot(x, y)
plt.show()

# Puts equally spaced 100 points from -5 to 5
x = np.linspace(-5,5, 100)
print(x)
plt.plot(x, 2.7**(-x),'g-')
plt.plot(x,1-x + x**2/2)
plt.show()

plt.style.use('seaborn-poster')
plt.figure(figsize = (10,6))

x = np.linspace(-5,5,20)
plt.plot(x, x**2, 'ko', label = 'quadratic')
plt.plot(x, x**3, 'r*', label = 'cubic')
plt.title(f'Plot of Various Polynomials from {x[0]} to {x[-1]}')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(loc = 4)
plt.show()


x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))

labels = ['First Order', 'Third Order', 'Fifth Order', 'Seventh Order']

plt.figure(figsize = (10,8))
for n, label in zip(range(4), labels):
    y = y + ((-1)**n * (x)**(2*n+1)) / np.math.factorial(2*n+1)
    plt.plot(x,y, label = label)

plt.plot(x, np.sin(x), 'k', label = 'Analytic')
plt.grid()
plt.title('Taylor Series Approximations of Various Orders')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()




import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (14, 8))
x = np.linspace(0,1,100)
y = np.zeros(len(x))
err = np.zeros(len(x))
labels = ['Zeroth Order', 'first Order', 'second Order','third order']


for ind in range(4):
    y = y + (-1)**(ind)*x**(ind)/np.math.factorial(ind)
    label = labels[ind]
    err = np.exp(-x) - y
    plt.subplot(2,1,1)
    plt.plot(x,err,label = label)
    plt.legend(loc=1)
    plt.ylabel('Error')
    plt.xlabel('x axis')
    plt.subplot(2,1,2)
    plt.plot(x,y,label = label)
    plt.ylabel('e^{-x}')
    plt.xlabel('x axis')
    plt.legend(loc=1)
    plt.grid()
    
plt.subplot(2,1,2)
plt.plot(x,np.exp(-x),label = 'Analytical')

plt.style.use('seaborn-poster') 
x = np.arange(11)
y = np.exp(-x)

plt.figure(figsize = (14, 8))



plt.semilogx(x,y)
plt.title('semilogx')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()


y = np.random.normal(0,5,100)
x = np.linspace(0,10,100)
ratio = 0.01
plt.plot(x,y)
avg = np.zeros(len(y)+1)
print(avg[2])
index = 0
for val in x:
    avg[index+1] = (1-ratio)*avg[index] + (ratio)*y[index]
    index  = index + 1

z = np.linspace(0,11,101)    
plt.plot(z,avg)
plt.grid()

plt.show()
    