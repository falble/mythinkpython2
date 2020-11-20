# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:07:47 2019

@author: Utente
"""

#Exercises Chapter 4 - TurtleWorld

#4.6 interface design 
import turtle
import math

bob = turtle.Turtle()
print(bob)

def poligon(t, lenght, n):
    angle = 360.0 / n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)
        
#def circle(t, r):
#    circumference = 2 * math.pi * r
#    n = 50
#    lenght = circumference / n
#    poligon(t, lenght, n)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    lenght= circumference / n 
    poligon(t, lenght, n)
    
circle(bob,100)

print('bravo stronzo')

turtle.mainloop()


