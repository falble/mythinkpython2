# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:57:45 2019

@author: Utente
"""
#Chapter 3 - Functions

#math functions

import math 

decibels = 10*math.log10(8)
print(decibels)
print(math.sqrt(81))
print(2*math.exp(2))

#composition

degrees = 45
x = math.sin(degrees/360.0*2*math.pi)

print(x)

#adding new functions

def print_lyrics():
    print("Hi I'm francesco and this is my course.")
    print("You can't look my page.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()

#parameters and arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)
    
print_twice('spam ')
print_twice('spam '*4)
repeat_lyrics()
print_twice(math.pi*9)

bocconi = 'trust me baby, internet non rende felici'
print_twice(bocconi)

#variables and parameters are local 

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    
line1= 'Faccetta nera '
line2= 'bella bissina.'
cat_twice(line1, line2)

#fruitful functions and void functions

result = print_twice('Bing')  
print(result) 


  

    
    