# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:47:08 2019

@author: Utente
"""

# Chapter 7 - Iteration

#7.1 Reassignment
#7.2 Updating variables
#7.3 The WHILE statement

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')
    
#countdown(10)
    
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2      #n is even
        else:              #n is odd
            n = n*3 + 1
            
#sequence(13)

def print_k(s, k):
    if k <= 0:
        return
    print(s)
    print_k(s, k-1)

s = "ah ah"
    
def print_n(s, n):
    while n != 0:
        print(s)
        n = n - 1
    
#print_n(s, 5)
        
#7.4 break
"""        
while True:        #the loop condition
    line = input('> ')
    if line == 'done':
        break
    print(line)
"""    
#print('Done!')
    
#7.5 Square roots

#iterate the formula y = (x + a/x) / 2
"""
x = 888
a = 25
epsilon = 0.000000000001
while True:
    print(x)
    y = (x + a/x) / 2
    if abs (y-x) < epsilon:
        break
    x = y
"""

#7.6 Algorithms


