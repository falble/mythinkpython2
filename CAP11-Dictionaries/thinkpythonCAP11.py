# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:54:41 2019

@author: Falble
"""

# Chapter 11 - Dictionaries 

# 11.1 A dictionary is a mapping

# similar to lists, but indices can be any type, contains a collection of indices, which are called KEYS,
# and a collection of values. Each key is associated with a single value. The association of a key and a value
# is called a key-value pair or sometimes an item. NB each key maps to a value.
# ex. a dictionary that maps from english to spanish words, so the keys and the values are all strings.

#eng2sp = dict() # creates a new dictionary with no items
#print(eng2sp)   # {}
#
#eng2sp['one'] = 'uno' # to add an item use []  NB one is the key uno is the value
#print(eng2sp)         # is true: 'one' in eng2sp; is true: 'uno' in vals

# 11.2 Dictionary as a collection of counters

# supposes you are given a string and you want to count how many times each letter appears.
# many ways: create 26 variables, create a list with 26 elements, create a dictionary keys=letters, value=counters
# same computation, but each implements that computation in a different way
# an IMPLEMENTATION is a way of performing a computation (some are better than others)
# ex. an advantage of the dictionary is that we don't have to know ahead of time wich letters appear in a string
# and we only have to make room for the letters that do appear.

#def histogram(s):
#    d = dict()
#    for c in s:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#    return d

#h = histogram('stocazzo')
#print(h)

# dictionaries have a method called get that takes a key and a default value, if the key appears return the
# corresponding value, otherwise it returns the default value.

#h = histogram('d')
#print(h)
#print(h.get('d',0))
#print(h.get('b',0))

# 11.3 Looping and dictionaries

#def print_hist(h):
#    for c in h:
#        print(c, h[c])
#
#h = histogram('supercalifragilistichespiralidoso')
#print_hist(h)

# to traverse the keys in sorted order
#def sorted_hist(h):
#    for key in sorted(h):
#        print(key, h[key])
#sorted_hist(h)

# 11.4 Reverse lookup

# given a dictioanary d and a key k, it easy to find the corresponding value v=d[k]. --> lookup
# but if you have v and you want to find k? 
# NB there might be more than one key that maps to the value v.
# NB there is no simple sintax to do a reverse lookup

#def reverse_lookup(d, v):    # NB reverse lookup is much slower than forward lookup
#    for k in d:
#        if d[k] == v:
#            return k
#    raise LookupError()
#    
#h = histogram('parrot')
#key = reverse_lookup(h,2)
#print(key)
#key = reverse_lookup(h,3)
#print(key)

# 11.5 Dictionary and lists

# lists can appear as values in a dictionary 

#def invert_dict(d):
#    inverse = dict()
#    for key in d:
#        val = d[key]
#        if val not in inverse:
#            inverse[val] = [key]
#        else:
#            inverse[val].append(key)
#    return inverse
#
#hist = histogram('scemotto')
#print(hist)
#inverse = invert_dict(hist)
#print(inverse)

# a dictionary is represented as a box with type dict above it and the key-value pairs inside

# 11.6 Memos

#known = {0:0, 1:1}  # is created outside the function so it belogns to the special frame __main__
#
#def fibonacci(n):
#    if n in known:
#        return known[n]
#    
#    res = fibonacci(n-1) + fibonacci(n-2)
#    known[n] = res
#    return res
#
#print(fibonacci(6))

# 11.7 Global variables

# --> __main__ variables are named global variables, which persist from one function call to next.
# --> FLAGS--> boolean variables that indicate wheter a condition is true 

#verbose = True 
#
#def example1():
#    if verbose:
#        print('Running example1')

#been_called = False
#
#def example2():
#    been_called = True # WRONG
#    
#been_called = False

#count = 0

#def example3():
#    count = count + 1 # WRONG
#
#print(example3())

#def example3():
#    global count
#    count += 1
#    
#print(example3())

#known = {0:0,1:1}
#
#def example4():
#    known[2] = 1
#
#def example5():
#    global known
#    known = dict()
    
