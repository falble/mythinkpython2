# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:11:33 2019

@author: Utente
"""

#Chapter 5 
#Exercise 5.6

import turtle


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)   

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)
    
bob = turtle.Turtle()

bob.pu()
bob.goto(-100, 50)
bob.pd()

snowflake(bob, 335)

turtle.mainloop()

