# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:30:00 2019

@author: Utente
"""

# Chapter 10 - Lists

# 10.1 a list is a sequence 

list_1 = [10, 20, 30, 40] # a list of four integers
list_2 = ['crunchy frog', 'ram bladder', 'lark vomit'] # a list of three strings
list_3 = ['spam', 2.0, 5, [10, 20]] # nested list
list_4 = [] # empty list

#print(list_3[3])

# 10.2 lists are mutable 

list_3[0] = 'spam assoreta'
#print(list_3)

# 10.3 Traversing a list

cheeses = ['Cheddar', 'Edam', 'Gouda']
#for cheese in cheeses:  # the for loop works weel if you only need to read the elements of the list
    #print(cheese)

# if you want to write or update the elements, you need the indices
"""
numbers = [1, 7, 23, 88]
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2
    print(i)
"""
# this loop traverses the list and updates each element. len returns the number of elements in the list.
# range returns a list of indices from 0 to n-1, where n is the lenght of the list. 
# each time through the loop i gets the index of next element. The assignment statement in the body uses i to read
# the old value of the element and to assign the new value
    
# NB: a for loop over an empty list never runs the body 
for x in []:
    print('This never happens')
    
# 10.4 List operations
    
# +
a = [1, 2, 3]
b = [5, 6, 7]
c = [4]
d = a + c + b
#print(d)
# * 
f = a * 3 
#print(f)

# 10.5 List slices

t = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(t[1:3], t[:4], t[4:], t[:])

# 10.6 List methods

#t.append("if i'm to fall") 

#t2 = ['7','cento'] 

#t.append(t2) # append a list
#t.extend(t2) # append list elements

tnove = ['OTTO', 'nove', 'dieci', 'undici', 'Dodicimila']
#tnove.sort()
#print(tnove) 

# 10.7 Map, filter and reduce
"""
def add_all(t):
    total = 0
    for x in t: 
        # accumulator
        total += x      # augmented statement: is equal to total = total + x
"""
"""
l = [1,2,3,7]  
print(sum(l))  # an operation that combines a sequence of elements into a single
                # value is sometimes called reduce
"""
"""                
def capitalize_all(tnove):     # an oparation like this is sometimes called a map
    res = []                   # because it maps a function onto each of the elements
    for s in tnove:
        res.append(s.capitalize())
    return res

print(capitalize_all(tnove))
"""
"""
# another common operation is to select some of the elements from a list and return 
# a sublist.

def only_upper(tnove):           # an operation like only_upper is called filter
    res = []                     # because it selects some of the elements and filters
    for s in tnove:              # out the others.
        if s.isupper():
            res.append(s)
    return res 

print(only_upper(tnove))
print(tnove)
"""
# 10.8 Deleting elements

#s = ['a','b','c'] 

#del s[2]
#print(s)

#s.remove('c')
#print(s)

#y = ['non ho', 'più', 'bisogno', 'internet', 'abbatte i confini']
#del y[0:3]
#print(y)

# 10.9 List and strings

# to convert a string in a list of characters --> list
s = 'nculo a mammt'

#t = list(s)
#print(s)
#print(t)

# to split
#t = s.split()
#print(t)

#fmf = 'filippo-vieni-a-cena'
#separator = '-'
#t = fmf.split(separator)
#print(t)

# join is the inverse of split
#t1 = ['ggg',':','il grande gigante']
#delimiter = ' '
#v = delimiter.join(t1)
#print(v)

# 10.10 Objects and values

# if you run assignment statement
# we know that a and b refer to a string, but we dont know whether they refer
# to the same string.

#a = 'banana'
#b = 'banana'
#print(a is b)

# but lists are two different object
#a = [1,2,3]               # we would say that two lists are equivalent, because they
#b = [1,2,3]               # have the same elements, but not identical, because they
#print(a is b)             # are not the same object

# 10.11 Aliasing

# if a refers to an object and you assign b = a, then both variables refer the same object
a = [1,2,3]
b = a
#print(b is a)

#b[0] = 'duce'
#print(a)

# 10.12 List argument

#def delete_head(t):
#    del t[0]
#
#letters = ['a','b','c','d']
#delete_head(letters)
#print(letters)

# NB: it is important to distinguish between oparations that modify lists and oparations that create
# a new lists. The append method modifies a list, but the + operator creates a new list.
#t1 = [1,2]
#t2 = t1.append(3)
#print(t1)
#print(t2)
#
#t3 = t1 + [4]
#print(t1)
#print(t3)

# an alternative is to write a function that creates and returns a new list.
#a = [1,2,3,4]
#def tail(t):
#    return t[1:]
#rest = tail(a)
#print(rest)

