# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:21:25 2022

@author: BATMAN1
"""

#Python Booleans

print(19>0)
print(11<4)
print(0==0)

a=200
b=33
if a>b:
    print("a is greater than b")

else:
    print("a is not greater than b")
    
    
    
print(bool(None))
print(bool(0))
print(bool(False))
print(bool())
print(bool(5))

print(bool(["apple", "cherry", "banana"]))

class myclass():
    def __len__(self):
        return 1

myobj=myclass()
print(bool(myobj))
    
