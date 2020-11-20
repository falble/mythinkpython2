# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:48:15 2019

@author: Utente
"""

#Exercises Chapter 3 

#3.2 do_four

def do_twice(func, arg):
    
    func(arg)
    func(arg)
    
def print_twice(arg):
    
    print(arg)
    print(arg)


def do_four(func, arg):
    
    do_twice(func, arg)
    do_twice(func, arg)
    
    
do_twice(print_twice, 'cazzo vuoi')
print('')

do_four(print_twice, 'cazzo vuoi')

#3.3 grid

def re_do_twice(f):
    f()
    f()
    
def re_do_four(f):
    re_do_twice(f)
    re_do_twice(f)
    
def print_beam():
    print('+ - - - -', end=' ')
    
def print_post():
    print('|        ', end=' ')
    
def print_beams():
    re_do_twice(print_beam)
    print('+')

def print_posts():
    re_do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    re_do_four(print_posts)
    
def print_grid():
    re_do_twice(print_row)
    print_beams()
    
print_grid()

#3.3 grid part two

def one_four_one(f, g, h):
    f()
    re_do_four(g)
    h()

def print_A():
    print('+', end=' ')

def print_Z():
    print('-', end=' ')

def print_C():
    print('|', end=' ')

def print_O():
    print('O', end=' ')

def print_end():
    print(' ')

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_Z, print_A)

def print1post():
    one_four_one(nothing, print_O, print_C)

def print4beams():
    one_four_one(print_A, print1beam, print_end)

def print4posts():
    one_four_one(print_C, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()



    

