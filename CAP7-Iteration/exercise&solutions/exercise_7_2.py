# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:58:45 2019

@author: Utente
"""

#Chapter 7 - Iteration 
#Exercise 7.2 

import math

def eval_loop():
    while True:
        n = input('---> ')
        if n == ' done' :
            break
        else:
            result = eval(n)
            print(result)
    print(result)

eval_loop()