# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:47:58 2019

@author: Utente
"""
#Exercise 4.2 - Flowers

import turtle 

from polygon import arc

def petal(t, r, angle):
    """Draws a petal using two arcs. 
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
    
    
def flower(t, n, r, angle):
    """Draws flower with n petals
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
 
    
def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()
bob.speed(10)

# draw a sequence of three flowers, as shown in the book.
#move(bob, -100)
#flower(bob, 7, 60.0, 60.0)

#move(bob, 100)
#flower(bob, 10, 40.0, 80.0)

#move(bob, 100)
#flower(bob, 20, 140.0, 20.0)

#move(bob, -300)
#flower(bob, 20, 140.0, 20.0)

#move(bob, -100)
#flower(bob, 15, 50.0, 70.0)

#move(bob, 500)
#flower(bob, 15, 55.0, 65.0)


bob.hideturtle()
turtle.mainloop()

   