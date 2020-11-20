# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:50:03 2019

@author: Utente
"""

#Exercise 4.5 - Spirals
import turtle


def draw_spiral(t, n, length=1, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.
    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)
    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.rt(dtheta)
        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=3000)

turtle.mainloop()
