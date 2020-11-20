# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:24:27 2019

@author: Utente
"""

#Chapter 5
#Exercise 5.3

def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > b + a):
        print('\nNo, unfortunately you are a dumb ass toy')
    else:
        print('\nYes, abc is a triangle')
        
def insert_sticks():
    a = int(input('Insert here the length of a = '))
    b = int(input('Now b = '))
    c = int(input('At least, pls, insert c = '))
    return is_triangle(a, b, c)

insert_sticks()
       