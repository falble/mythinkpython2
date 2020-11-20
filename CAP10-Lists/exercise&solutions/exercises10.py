# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:20:30 2019

@author: Falble
"""

# Exercise 10.1 - nested_list

# write a function called nested_sum that takes a list of lists of integers and adds up the elements
# from all of the nested lists.

#nested_list = [1, 2, [3,[ [ 5 , 6, [ 5 ] ], 4], 5, [6, 7]]]
#t = [[1,2],[3],[4,5,6]]
#
#def nested_add_all(t): 
#    
#    total = 0
#    for x in t:
#        if type(x)==list:
#          total += nested_add_all(x)
#        else:
#          total += x
#    return total
#
#print(nested_add_all(t))

# Exercise 10.2 - cumsum

# write a function that takes a list of numbers and returns the cumulative sum

#t = [1,2,3,8,12,4,5]
#
#def cumsum(t):
#    result = []
#    total = 0
#    for element in t:
#        total += element
#        result.append(total)
#    return result
#
#print(cumsum(t))

# Exercise 10.3 - middle

# takes a list and returns a new list that contains all but the first and last elements

#t = [1,2,3,4,5,6,7,8,9,10]
#
#def middle(t):
#    return t[1:-1]
#
#middle = middle(t)
#print(middle)

# Exercise 10.4 - chop

# takes a list, modifies it by removing the first and the last and returns None

#t = [1,2,3,4]
#
#def chop(t):
#    del t[1]
#    del t[-1]
#    
#print(t)
#print(chop(t))
#print(t)

# Exercise 10.5 - is_sorted

# takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise

#def is_sorted(t):
#    return t == sorted(t)
#
#
#print(is_sorted([1, 2, 2]))
#print(is_sorted(['b', 'a']))
#print(is_sorted(['a', 'a']))
#print(is_sorted(['a', 'b']))
#print(is_sorted([2, 1]))
#print(is_sorted([1, 2, 3, 4, 3]))

# Exercise 10.6 - is_anagram 

# write a function that takes two strings and returns True if they are anagrams 

#def is_anagram(text1, text2):
#    return sorted(text1) == sorted(text2)
#
#print(is_anagram('abba','baba'))
#print(is_anagram('tiziano','notizia'))
#print(is_anagram('jenny','jelly')) 

# Exercise 10.7 - has_duplicates

# Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should not modify the
# original list.


#def has_duplicates(t):
#    if len(t) == 0:
#        return "List is empty."
#    elif len(t) == 1:
#        return "List contains only one element."
#    
#    previous_elem = t[0]
#    for elem in sorted(t):
#        if previous_elem == elem:
#            return True
#        previous_elem = elem
#    return False
#
#
#t = [4, 7, 2, 7, 3, 8, 9 ]
#print(has_duplicates(t))
#print(has_duplicates(['b', 'd', 'a', 't']))
#print(has_duplicates([]))
#print(has_duplicates(['']))
#print(has_duplicates([5, 7, 9, 2, 4, 1, 8,]))




