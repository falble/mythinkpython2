# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:35:10 2019

@author: Falble
"""

# Exercise 13.5

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('stocazzo')
print(h)

import random

def choose_from_hist(d):
    res = []
    for key in d:
        for i in range(d[key]):
            res.append(key)
    return random.choice(res)

print(choose_from_hist(h))

MAX_TESTS = 100000

import collections

def main():
    # Create a dictionary to store random test results
    result_dict = dict()

    # Create a test historgram
    test_hist = histogram('stocazzo')
    print(test_hist)
    # Repeat the operation a large number times, see if it aligns with 
    # percentage a char appears. 
    for index in range(MAX_TESTS):
        chosen_value = choose_from_hist(test_hist)
        # We use set default to either add or modify current dictionary value
        result_dict[chosen_value] = result_dict.setdefault(chosen_value,0) + 1
        # We sort the dictionary using the 'collections' module
        sorted_result_dict =  collections.OrderedDict(sorted(result_dict.items(), reverse=True, key=lambda t: t[1]))
    # Print our results, the char, and percentage of times encountered.
    for key, value in sorted_result_dict.items():
           print("%s: %s" % (key, (float(value)/MAX_TESTS) * 100))

if __name__ =='__main__':
    main()