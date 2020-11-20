# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:19:44 2019

@author: Utente
"""

#Chapter 8 - Strings
#Exercise 8.3

# fruit = 'banana'
# fruit[0:5:2]
# 'bnn'
#NB: [::-1] generates a reverse string

first_word = input('Write the word to compare: ')

if first_word == first_word[::-1]:
    print('Is a palindrome: ' + first_word[::1] +'!!!')
else:
    print(first_word + ' is not a palindrome')

