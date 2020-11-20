# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:34:52 2019

@author: Falble
"""

# Exercise 15.1

import math
import copy

class Point:
    """Represents a point in 2-D space."""
    


def print_point(p):
    print('(%g, %g)'%(p.x, p.y))


def distance_between_point(p1,p2):
    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    print('p1 is (%g, %g) '%(p1.x, p1.y))
    print('and p2 is (%d, %d).'%(p2.x, p2.y))
    print('the distance is ',distance)
    return distance



class Rectangle:
    """Represents a rectangle.

    attrinutes: width, height, corner.
    """
    
    

class Circle:
    """Represents a circle in 2-D spaces.
    
    attributes: center, radius.
    """


    
def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    d = distance_between_point(point, circle.center)
    print(d)
    if d <= circle.radius:
        print('d is inside the circle')
    else:
        print('d is an immigrant')
    
    return 


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """    
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True        
    
        
def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False    


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0
    
    print('box.corner.x is ',box.corner.x)
    print('box.corner.y is ',box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print('the x of circle center is ',circle.center.x)
    print('the y of circle center is ',circle.center.y)
    print('the radius is ',circle.radius,'\n')

#    print(point_in_circle(box.corner, circle))
#    print(rect_in_circle(box, circle))
#    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()