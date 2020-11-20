# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:30:23 2019

@author: Falble
"""

# Chapter 13 - Case study: data structure selection

# 13.1 Word frequency analysis

# exercise 13_1
# exercise 13_2 --> gutemberg.py
# exercise 13_3
# exercise 13_4

# 13.2 Random numbers

# we want the computer to be unpredictable. Games are an obvious example. Making a program truly nondeternistic
# turns out to be difficult, but there are ways to make it at least seem nondeterministic.
# --> use algorithms that generate pseudorandom numbers. # random module

#import random

# random.random returns a random float between 0.0 and 1.0

#for i in range(3):
#    x = random.random()
#    print(x)

# radom.randint, takes two parameters low and high and returns an integer between them (including both)

#print(random.randint(5,10))
#print(random.randint(5,10))

# to choose an element from a sequence at random, you can use .choice

#t = [1,2,3]
#print(random.choice(t))

# exercise 13_5

# 13.3 Word histogram

# here is a program that reads a file and builds a histogram of the words in the file:

import string

# loops through the lines of the file, passing them one at a time to process_line. 
def process_file(filename):
    hist = dict() # hist is used as an accumulator
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

# uses the string method replace ('-' --> ' ') 
def process_line(line, hist):
    line = line.replace('-',' ')
    # removing punctuation and convert to lower case
    # NB strings are not converted (they are immutable) --> strip and lower return new strings
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0)+1
        
hist = process_file('emma.txt')

# to count the total number of words in the file, we can add up the frequencies in the histogram
def total_words(hist):
    return sum(hist.values())

# the number of different words is just the number of items in the dictionary
def different_words(hist):
    return len(hist)

# here is some code to print the result
print('Total number of words:', total_words(hist))
print('Number of different words:', different_words(hist),'\n')
##print(hist)

# 13.4 Most common words

# to find the most common words, we can make a list of tuples, where each tuple contains a word
# and its frequency, and sort it. The following function takes a histogram and returns a list of word-freq. tuples
def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value,key))
        
    t.sort(reverse = True)
    return t

# in each tuple, the frequency appears first, so the resulting list is sorted by frequency. 
# here is a loop that prints the ten most common words
#t = most_common(hist)
#print('The most common words are:')
#for freq, word in t[:10]:
#    print(word, freq, sep='\t')
    
# 13.5 Optional parameters

def print_most_common(hist, num=10):  # NB all the required parameters have to come first, followed by the optional ones
    t = most_common(hist)
    print('The most common',num,'words are:','\n')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')
    print('\n')
print_most_common(hist) # if you only provide one argument--> num=default value
#print_most_common(hist,20) # if you provide two arguments--> the optional argument overrides the default value

# 13.6 Dictionary subtraction

# finding the words from the book that are not in the word list is a problem you might recognize as set 
# subtraction; that is, we want to find all the words from one set that are not in the other
def subtract(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key]=None
    return res

# we can use process_file to build a histogram for words.txt, and the subtract
words = process_file('words.txt')
diff = subtract(hist,words)

#print("Words in the book that aren't in the word list:",'\n')
#for word in diff:
#    print(word, end=' ')
#print('\n')

# 13.7 Random words

# to choose a random word from the histogram, the simplest algorithm is to build a list with multiple
# copies of each word, according to observed frequency, and then choose from the list:
import random

def random_word(h):
    t=[]
    for word, freq in h.items():
        t.extend([word] * freq)
    
    return random.choice(t)

print('Random word from the book','\n')
print(random_word(hist))

# 13.8 Markov analysis 

# one way to measure these kind of relationships is markov analysis, which characterizes, for a given sequence 
# of words, the probability of the words that might come next. 

# exercise 13_8 --> markov analysis
 
# 13.9 Data structures 

