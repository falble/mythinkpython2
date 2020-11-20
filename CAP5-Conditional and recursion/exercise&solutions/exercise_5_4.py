# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:52:53 2019

@author: Utente
"""

#Chapter 5
#Exercise 5.4

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
recurse(2, 0)
