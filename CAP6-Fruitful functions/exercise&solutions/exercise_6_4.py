# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:41:43 2019

@author: Utente
"""

#Chapter 6 - Fruitful function
#Exercise 6.4

#is_power
def is_power(a,b):
    # trivial case
    if (a==b): return True

    # Exception Handling
    if (b==0) or (b==1): return False # unless a==b==0 or a==b==1, which are handled by the trivial case above

    # recursive case
    return ((a%b)==0) and (is_power(a/b,b))
    
print(is_power(30, 3))