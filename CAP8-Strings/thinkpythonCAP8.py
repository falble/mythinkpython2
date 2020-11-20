# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:23:49 2019

@author: Utente
"""

#Chapter 8 - Strings

#8.1 A string is a sequence 
#8.2 len
#8.3 Trasversal with a for loop
"""
fruit = 'banana'
index = 3 
while index < len(fruit):
    letter = fruit[index] #VARIABLE = letter
    print(letter)
    index = index + 1
    
print('\n')   

for letter in fruit:
    print(letter)
    
print('\n')

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'J':
        print(letter + suffix)
"""       
#8.4 String slices 
#8.5 Strings are immutable
#8.6 Searching
"""
#what does this function

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1 
    return -1
"""
#8.7 Looping and counting
"""
word = 'banana fascista nazista razzista'
count = 0
for letter in word:
    if letter == 'a':
        count = count +1
print(count)
"""       
#8.8 Strings methods
#8.9 The in operator 
        
#the following function prints all the letters from word1 that also appear in word2
"""    
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')
"""
#8.10 String comparison
#word = 'banana' 
#if word == 'banana':
#    print('All right, bananas!')

#for Python all the uppercase letters come before all the lowercase letters
"""
word = 'Oranges'     
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas!!')
"""
#8.11 Debugging 
"""
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)-1   #because the first position is 0 not 1!!!!

    while j > 0:
        print(i, j)    # print here
        
        if word1[i] != word2[j]:
            return False
        i = i+1 
        j = j-1

    return True

is_reverse('pots', 'stop')
"""
            
