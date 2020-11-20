# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:26:15 2019

@author: Falble
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__' :
    print(linecount('wc.py'))