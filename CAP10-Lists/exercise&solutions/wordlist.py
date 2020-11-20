# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:22:50 2019

@author: Falble
"""

#import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

print(make_word_list1())

#def make_word_list2():
#    """Reads lines from a file and builds a list using list +."""
#    t = []
#    fin = open('words.txt')
#    for line in fin:
#        word = line.strip()
#        t = t + [word]
#    return t
#
#print(make_word_list2())


#start_time = time.time()
#t = make_word_list1()
#elapsed_time = time.time() - start_time
#
#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')
#
#start_time = time.time()
#t = make_word_list2()
#elapsed_time = time.time() - start_time
#
#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')