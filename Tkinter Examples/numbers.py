# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:40:06 2022

@author: BATMAN1
"""

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100

print(type(x),x)
print(type(y),y)
print(type(z),z)

a = 3+5j
print(type(a),a)

import random

print(random.randrange(1, 10))