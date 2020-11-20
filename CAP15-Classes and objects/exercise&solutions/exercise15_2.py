# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:21:42 2019

@author: Falble
"""

# Exercise 15.2

import turtle

from exercise15_1 import Point, Rectangle, Circle

import polygon

def draw_circle(t, circle):
    """Draws a circle.

    t: Turtle
    circle: Circle
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t, circle.radius)
    
def draw_rect(t, rect):
    """Draws a rectangle.

    t: Turtle
    rect: Rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)


if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw the axes
    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    # draw a rectangle
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    draw_rect(bob, box)

    # draw a circle
    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    draw_circle(bob, circle)

    # wait for the user to close the window
    turtle.mainloop()