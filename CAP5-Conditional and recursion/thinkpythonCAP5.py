# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 23:40:22 2019

@author: Utente
"""

#Chapter 5 - Conditionals and recursion
#Conditional execution
x = -777
if x > 0 :
    print('x is positive Sir, this is x:')
    
#Alternative conditions
else : 
    print('FUCK you Sir x is negative' )
    
#Chained conditions
x = 12
y = 12
if x > y :
    print('x is greater than y, Sir')
elif x < y:
    print('Sir your number is less than y')
else:
    print('pareggiotto')
    
#Nested conditions
a = 89
b = 19
if a == b :
    print('a and b are equal')
else:
    if a < b : 
        print('ah ah bad luck')
    else:
        print(a,'is greater than', b)

d = 12
c = 9       
if 100 < d and c < 30:
    print('nothing alright')
else:
    print('loser')
    
#you can write
alfa = 5
if 0 < alfa < 9:
    print('good')
    
#recursion

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
# since is greater than zero!!
s = 'duce duce duce duce duce duce duce duce duce duce duce'

def print_k(s, k):
    if k <= 0:
        return
    print(s)
    print_k(s, k-1)
    
#print_k(s, 14)

    
#Infinite recursion
    
#def recurse():
    #recurse()


#Keyboard input
    
import math 
signal_power = 90 
noise_power = 10
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print(decibels)


    
