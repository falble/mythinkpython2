# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:05:38 2019

@author: Utente
"""

#Chapter 6 - Fruitful function
#Exercise 6.1

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y + 3, x + y))


    