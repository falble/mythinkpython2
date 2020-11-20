# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:34:57 2019

@author: Utente
"""

#Exercises Chapter 4 - TurtleWorld

#4.5 Generalization
import turtle

bob = turtle.Turtle()
print(bob)

def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)
        
square(bob, 350)

turtle.mainloop()

#4.5 Generalization_2 (poligon)
import turtle

bob = turtle.Turtle()
print(bob)

def poligon(t, lenght, n):
    angle = 360.0 / n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

poligon(bob, 85, 12)

turtle.mainloop()