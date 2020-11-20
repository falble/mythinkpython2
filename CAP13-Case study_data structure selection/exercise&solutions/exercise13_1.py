# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:39:41 2019

@author: Falble
"""

# Exercise 13.1
# write a program that reads a file, breaks each line into words, strip whitespaces and punctuation
# from the words and converts them to lowercase

import string

#print(string.punctuation)
punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]
 
#split into words
def words():
    data = open('adult_data.txt', 'r')
    main = []
    for line in data:
        for item in line.split():
            main.append(item)
    return main
    data.close()
 
#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuations) or (char in whitespaces)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
         
print("The book has %s 'words'" % len([clean(word) for word in words()]))