# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:14:25 2019

@author: Utente
"""

#Chapter 6 - Fruitful function
#Exercise 6.2

#The Ackermann function A(m, n)

"""
In computability theory, the Ackermann function, named after Wilhelm Ackermann, 
is one of the simplest[1] and earliest-discovered examples of a total computable 
function that is not primitive recursive. All primitive recursive functions are 
total and computable, but the Ackermann function illustrates that not all total 
computable functions are primitive recursive.

After Ackermann's publication[2] of his function (which had three nonnegative integer arguments),
many authors modified it to suit various purposes, so that today "the Ackermann function" may 
refer to any of numerous variants of the original function. One common version, the two-argument
Ackermann–Péter function, is defined as follows for nonnegative integers m and n
"""

def ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m , n -1))
    
print(ackermann(3, 8))
        