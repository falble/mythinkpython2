# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:34:12 2019

@author: Utente
"""

#Exercises Chapter 4 - TurtleWorld

#4.4 Encapsulation
import turtle

bob = turtle.Turtle()
print(bob)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)

alice = turtle.Turtle
square(alice)

        

