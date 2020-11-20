# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:52:57 2019

@author: Utente
"""

# Chapter 9 - Case study: word play

# Reading word lists
"""
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
"""

# Exercise 9.1
"""
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
"""

# Exercise 9.2 
# ??

# Search 
# watch the copybook

# Looping with indices 
"""
def is_palindrome(word):
    
    i = 0
    j = len(word) - 1
    
    while i < j:
        if word[i] != word[j]:
            print('no')
            return False
        i = i + 1
        j = j - 1
    print('yes')   
    return True

is_palindrome('anna')
"""
