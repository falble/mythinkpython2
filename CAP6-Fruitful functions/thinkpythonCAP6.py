# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:41:11 2019

@author: Utente
"""

#Chapter 6 - Fruitful functions

#6.1 Return values

import math 

#e = math.exp(1.0)

#radius = 10
#radians = 45.0
#height = radius * math.sin(radians)

def area(radius):
    a = math.pi * radius**2
    return a

#print(area(10))

#def area(radius):
#    return math.pi * radius**2

#print(area(10))
    
#def absolute_value(x):
#    if x < 0:
#        return -x
#    else:
#        return x
    
#print(absolute_value(0))

#print(abs(-9))
        
#small exercise
        
#def compare_functions(x, y):
#    if x > y:
#        return print('1')
#    elif x == y:
#        return print('0')
#    else:
#        return print('-1')
    
#compare_functions(4, 3)
        
#6.2 Incremental development
#return 0.0
#dx dy
#squaring
#math.sqrt

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    length = math.sqrt(dsquared)
    print('The distance is: ', length)
    return length

#distance(1, 2, 4, 6)
    
#6.3 Composition
    

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    print('The circle area is: ', result)
    return result


#circle_area(1, 5, 3, 8)

#shorter way

def circle_area_2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

#print('The circle area is ',circle_area_2(1, 5, 3, 8))
    

#6.4 Boolean functions
    
#def is_divisible(x, y):
#    if x % y == 0:
#        return True
#    else: 
#        return False
    
#print(is_divisible(6, 4))

def is_divisible(x, y):
   return x % y == 0

#print(is_divisible(8, 4))

#small exercise
   
def is_between(x, y, z):
    if (x <= y) and (y <= z):
        return True 
    else:
        return False
    
#print(is_between(7, 2, 9))
        

#6.5 More recursion
        
#def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
#print(factorial(6))


#6.6 Leap of faith
        
#6.7 One more example
#Fibonacci's number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
#print(fibonacci(15))
    
#6.8 Cheeking type             #isinstance(obj, class_or_tuple, /)
                               # Return whether an object is an instance of a class or of a subclass thereof.   
                               # A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
                               # check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
                               #or ...`` etc.
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(0))