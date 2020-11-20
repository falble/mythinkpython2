# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:11:27 2019

@author: Utente
"""

#Chapter 8 - Strings
#Exercise 8.2

word = 'Banana'
letter = 'n'
counter = word.count(letter)
if counter == 0:
    print('In word there is no a')
elif counter == 1:
    print('In word there is one a')
else:
    print('In word there are ' + str(counter) + ' '  + str(letter))
    
