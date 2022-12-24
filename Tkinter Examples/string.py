# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:53:11 2022

@author: BATMAN1
"""

#string

a="adarsh tayde"
print(a)

#to print multiple lie use """(triple double code or single code)

b="""Text Free is an application made by Pinger 
 that allows users to text and call over the
 internet for free or for a price. 
 The application runs on iOS, Android, 
 Microsoft Windows and Macintosh devices.
 Competitors include GOGII, Optini and WhatsApp."""
print(b)

#Strings are Arrays
x="Adarsh"
print(x[1])

#loop in string

for x in "banana":
    print(x)
    
#length of string
x="adarsh"
print(len(x))

#Check String
x="india is my cpuntry all indian are my"
print("india"in x)


#print if present
x="india is my cpuntry all indian are my"
if "india"in x:
    print("word india is present")
    
#Check if NOT

x="india is my cpuntry all indian are my"
if "japan"not in x:
    print("word japan is not present")
    