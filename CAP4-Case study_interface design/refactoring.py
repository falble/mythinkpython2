# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:36:25 2019

@author: Utente
"""

#Exercises Chapter 4 - TurtleWorld

#4.7 refactoring 
import turtle
import math

bob = turtle.Turtle()
print(bob)

#def arc(t, r, angle):                                    #copy poligon and transform it into arc
#    arc_lenght = 2 * math.pi * r * angle / 360
#    n = int(arc_lenght / 3) + 1
#    step_lenght = arc_lenght / n
#    step_angle = angle / n 
    
#    for i in range(n):
#        t.fd(step_lenght)
#        t.lt(step_angle)

def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

def poligon(t, lenght, n):
    angle = 360.0 / n
    polyline(t, n, lenght, angle)
    
def arc (t, r, angle):
    arc_lenght = 2 * math.pi * r * angle / 360
    n = int(arc_lenght / 3) + 1 
    step_lenght = arc_lenght / n 
    step_angle = float(angle) / n 
    polyline(t, n, step_lenght, step_angle)
    
#we can rewrite circle using arc
    
def circle (t, r):
    arc (t, r, 360)
    
circle(bob, 70)

print('Cerchio perfetto chiamami Giotto')

turtle.mainloop()   
