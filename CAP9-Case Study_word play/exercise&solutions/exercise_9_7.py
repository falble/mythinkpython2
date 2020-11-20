# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:42:15 2019

@author: Utente
"""

# Chapter 9 - Case study: word play
# 9.7

def is_triple_double(word):
    
    i = 0
    count = 0
    
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False

def find_triple_double():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)
            
            
print('Here are all the words in the list that have')
print('three fucking consecutive doubles letters')
find_triple_double()
print('')