# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:02:40 2019

@author: Utente
"""

#Chapter 5
#Exercise 5.5

import turtle 

bob=turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
    
draw(bob, 15, 7)

turtle.mainloop()
