# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:19:01 2019

@author: Utente
"""

#Chapter 4 - Case study: interface design
#Exercise 4.1

import turtle
import math

bob = turtle.Turtle()
print(bob)

def arc(t, r, angle):                                    #copy poligon and transform it into arc
    arc_lenght = 2 * math.pi * r * angle / 360
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n 
    
    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)
        
arc(bob, 130, 360)