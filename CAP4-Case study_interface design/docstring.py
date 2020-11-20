# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:36 2019

@author: Utente
"""

#Chapter 4
#docstring

import turtle
import math

bob = turtle.Turtle()
print(bob)

def polyline(t, n, lenght, angle):
    #documentation string--->
    """Draws n line segments with the given lenght  
    and angle (in degrees) between them. 
    t is a turtle.
    """
    #the aim is to simplify the code and to improve interface design
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)
    
polyline(bob, 4, 120, 90) #preconditions of the functions (should be satisfied by the caller)

turtle.mainloop() #in this case the square is the postcondition (should be satisfied by the function)
                  #intended effect  (the segments)
                  #any side effects (like moving the turtle)
