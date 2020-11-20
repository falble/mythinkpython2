# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:44:59 2019

@author: Utente
"""

#Chapter 7 - Iteration
#Exercise 7.1


import math

def mysqrt(a):
    x = a/5
    while True:
        y = (x+ a/x) / 2
        if y == x:
            return x
        x = y

def test_square_root():
    a = 1.0
    print('a', repr(mysqrt(a)).rjust(6), repr(math.sqrt(a)).rjust(12), 'diff'.rjust(10))
    print("-      ---------            ------------          ----")
    while a < 10.0:
        print(a, "  ", mysqrt(a), "  ", math.sqrt(a), "  ", abs(mysqrt(a)-math.sqrt(a)))
        a += 1

test_square_root()