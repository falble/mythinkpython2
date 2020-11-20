# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:06:38 2019

@author: Utente
"""

#Chapter 6 - Fruitful function
#Exercise 6.5

#The greatest common divisor (GCD)

def gcd_francesco(a,b):
    if b == 0:      #base case gcd(a,0)=a
        return a
    return gcd_francesco(b, a%b)  #gcd(a,b)=gcd(b,remainder)

print(gcd_francesco(80,45))

#import gcd 
from fractions import gcd
print(gcd(80,45))