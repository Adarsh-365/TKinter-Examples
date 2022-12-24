# -*- coding: utf-8 -*-

from math import *    
posx, posy = 0,0    
sides = 32    
radius = 1    
  
for i in range(100):    
    cosine= radius * cos(i*2*pi/sides) + posx    
    sine  = radius * sin(i*2*pi/sides) + posy    
    print(cosine,sine)