# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:59:21 2019

@author: Utente
"""

# Chapter 9 - Case study: word play
# 9.8

def has_palindrome(i, start, length):
    
    s = str(i)[start:start+length]
    
    return s[::-1] == s


def check(i):
    
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))
    

def check_all():
    
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()