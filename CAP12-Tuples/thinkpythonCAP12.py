# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:03:22 2019

@author: Falble
"""

# Chapter 12 - Tuples

# built-in type, the tuple, and then shows how lists, dictionaries, and tuples work together.

# 12.1 Tuples are immutable

# a tuple is a sequence of values, they can be any type, and they are indexed by integers, they are similar
# to lists but they're immutable. Tuple is a coma separeted list of values, it is common to enclose tuples in 
# parentheses. NB: to create a tuple with a single element t1 = 'a', !!!

#t = 'a','b',1,'r'
#print(type(t))
#t1 = 0,'e','sette'
#print(type(t1))

# NB
#t2 = 'a',
#print(type(t2))
#t3 = 'a'
#print(type(t3))

# another way to create tuple is the built-in function

#t = tuple()
#print(t)

# NB if the argument is a sequence (string, list or tuple)

#t = tuple('italotreno')
#print(t) # (return a tuple of letter, in this case)
#l = tuple([1,2,3,4,5])
#print(l)

# most list operators also work on tuples 
#print(t[0:5])
#print(l[0])

# but if you try to modify one of the elements of the tuple you get an error!! (they are immutable)

#l[0] = 12
#print(l)

# because tuple are immutable you can't modify them but you can replace one tuple with another 

#l = (12,) + l[1:]
#print(l)

# the relational operator work with tuples and other sequences; Python starts by comparing 
# the first element from each sequence. If they are equal, it goes to next elements, and so on,
# until it finds elements that differ. NB subsequent elements are not considered

#o = (0,1,2)
#o2 = (0,3,4)
#print(o<o2)
#o3 = (0,1,200000)
#print(o3<o2)

# 12.2 Tuple assignment

# to swap a and b (creating a temp variable) --> working on the console

#addr = 'monty@python.org'
#uname, domain = addr.split('@')
#print(uname)
#print(domain)

# 12.3 Tuples as return values

# NB a function can only return one value, but if the value is a tuple, the effect is the same 
# as returning multiple values.
# ex. you want to divide two integers and compute the quotient and remainder. 

#t = divmod(67,2) # divmod() is a built-in function that takes two arguments and return a tuple of two values (q,r)
#print(t)

# or use tuple assignment to store the elements separately

#quot, rem = divmod(67,2)
#print(quot)
#print(rem)

# ex. function that returns a tuple

#def min_max(t):
#    return min(t), max(t)
#
#t = (20,35,46,76,21,41,12,78)
#print(min_max(t))

# 12.4 Variable-lenght argument tuples

# NB a parameter name that begins with *gathers arguments into a tuple

#def printall(*args):
#    print(args)
#
#printall(1,2.0,'sette')

# NB the complement of gather is scatter. If you have a sequence of values and you want to pass it 
# to a function as multiple arguments

#t = (7,3)
#print(divmod(*t))

# many of the built-in functions use variable-lenght argument tuples

#print(max(9,4,13))

# 12.5 List and tuples

# zip is a built-in function that takes two or more sequences and returns a list of tuples where 
# each tuple contains one element from each sequence. 
# ex. zips a string and a list

#s = '6gay'
#t = [0,0.2,8,2]
#print(zip(s,t))

#for pair in zip(s,t):
#    print(pair)

# a zip object is a kind of iterator, which is any object that iterates through a sequence.
# if you want to use list operators and methods, you can use a zip object to make a list:

#print(list(zip(s,t))) # the result is a list of tuples, (in this case: each tuple containsa pair of values)

# NB if the sequence are not the same lenght, the result has the lenght of the shorter one
#print(list(zip('ANNE','elk')))

# you can use a tuple assignment in a for loop to traverse a list of tuples
#t = [('a',0),('b',1),('c',2)]
#for letter, number in t:
#    print(number,letter)

# ex.
#def has_match(t1,t2):
#    for x,y in zip(t1,t2):
#        if x == y:
#            return True 
#    return False
#
#t1 = tuple('italotreno')
#t2 = tuple('trenitalia')
#print(has_match(t1,t2))
#num = (1,3,4.0)
#l = tuple('filippo')
#print(has_match(num,l))

# if you need to traverse the elements of a sequence and their indices, you can use the built-in function enumerate

#for index, element in enumerate('abc'):
#    print(index, element)

# 12.6 Dictionaries and tuples

# dictionaries have a method called items, that returns a sequence of tuples, where each tuple is a key-value pair.

#d = {'a':0,'b':1,'c':2}
#t = d.items()
#print(t) # the result is a dict_items object, which is an iterator that iterates the key-value pairs.
#
#for key, value in d.items():
#    print(key, value)

# you can use a list of tuples to initialize a new dictionary

#t = [('a',0),('b',1),('c',2)]
#d = dict(t)
#print(d)

# combining dict with zip yields a concise way to create a dictionary

#d = dict(zip('abc',range(3)))
#print(d)
# NB dictionary method .update

# it is common to use tuples as keys in the dictionaries
#last = 'albertini'
#first = 'francesco'
#number = 666
#directory = {}
#directory[last,first] = number
#for last, first in directory:
#    print(first,last,directory[last,first])

# 12.7 Sequences of sequences 

# almost of the examples also work with lists of lists, tuples of tuples, and tuples of lists.
# Many times, the different kinds of sequences can be used interchangeably. So how should you choose one over
# the others? 
# STRINGS: the elements have to be characters, they are also immutable. If you need the ability to change
# the characters in a string, you might want to use a list of characters instead.
# LISTS are more common than tuples, mostly because they are mutable.
# NB case where you might prefer tuples:
# 1) in some contexts, like a return statement, it is syntactically simpler to create a tuple than a list.
# 2) if you want to use a sequence as a dictionary key, you have to use an immutable type like tuples or strings.
# 3) if you are passing a sequence as an argument to a function, using tuples reduces the potential, for 
#    unexpected behavior due to aliasing.

# 12.8 Debugging 
# lists, dictionaries and tuples are examples of data structures
# NB SHAPE ERRORS when a data structure has the wrong type, size or structure
# NB watch STRUCTSHAPE 

#from structshape import structshape
#
#t = [1,2,3]
#print(structshape(t))
#t2 = [[1,2],[3,4],[5,6]]
#print(structshape(t2))
#t3 = [1,2,3,4.0,'5','6',[7],[8],9]
#print(structshape(t3))
#s = 'abc'
#lt = list(zip(t,s))
#print(structshape(lt))
#d = dict(lt)
#print(structshape(d))

# !!! if you having trouble keeping track of your data structures, structshape can help !!!

