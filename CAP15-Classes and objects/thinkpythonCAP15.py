# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:38:35 2019

@author: Falble
"""

# Chapter 15 - Classes and objects 
#--> object oriented programming, to organize both code and data

# 15.1 Programmer-defined types
# we will create a type called Point that represents a point in two-dimensional space.
# different ways to represents points in python:
# - store the coordinates in two different variables, x and y
# - store the coordinates as elements in a list or tuple
# - create a new type to represent points as objects
# a programmer-defined type is also called a class. 

import math

class Point:
    """Represents a point in 2-D space.""" # explains what the class is
    
    
#print(Point)

blank = Point() # a class object is like a factory for creating objects
#print(blank)

# 15.2 Attributes

blank.x = 3.0
blank.y = 4.0
#print(blank.x)
#print(blank.y)
#
#print('(%g, %g)' % (blank.x, blank.y))
#
#distance = math.sqrt(blank.x**2 + blank.y**2)
#print(distance)

#sette = Point()
#sette.x = 7
#sette.y = 7 

def print_point(p):
    print('(%g, %g)'%(p.x, p.y))
#    
#print_point(blank)
#print_point(sette)

def distance_between_point(p1,p2):
    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    print('p1 is (%g, %g) '%(p1.x, p1.y))
    print('and p2 is (%d, %d).'%(p2.x, p2.y))
    print('the distance is ',distance)
#    
#distance_between_point(blank,sette)

# 15.3 Rectangles
# what attributes would you use to specify the location and size of a rectagle
# - you could specify one corner of the rectangle, the width, and the height.
# - you could specify two opposing corners.

class Rectangle:
    """Represents a rectangle.

    attrinutes: width, height, corner.
    """
#
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0 # go to objects box refers to and selct the attribute named corner, the go to that object box 
box.corner.y = 0.0 # refers to and select the attribute named x or y 

    
# 15.4 Instances as return values
# functions can return instances. for ex., find_center takes a Rectangle as an argument and return a Point that 
# that contains the coordinates of the center of Rectangle
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

#center = find_center(box)
#print_point(center)
    
# 15.5 Objects are mutable
# you can change the state of an object by making an assignment to one of its attributes. For example,
# to change the size of rectangle without changing its position, you can modify the values of width and height
    
#box.width = box.width + 50
#box.height = box.height + 100

# you can also write functions that modify objects. 

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    
#print(box.width, box.height)
#grow_rectangle(box, 50, 100)
#print(box.width, box.height)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    
#move_rectangle(box, 20, 20)
#print(box.corner.x,box.corner.y)

# 15.6 Copying
# the copy module contains a function called copy that can duplicate any object

#p1 = Point()
#p1.x = 3.0
#p1.y = 4.0

#import copy

#p2 = copy.copy(p1)

# p1 and p2 contains the same data, but they are not the same Point

#print_point(p1)
#print_point(p2)
#print(p1 is p2)
#print(p1 == p2) # surprise '==' is equivalent to 'is'

# if you use copy.copy to duplicate a rectangle, you will find that it copies the rectangle object but 
# not the embedded point.

#box2 = copy.copy(box)
#print(box2 is box)
#print(box2.corner is box.corner)

# shallow copy because it copies the object and any references it contains, but not the embedded objects.
# in this ex, invoking grow_rectangle on one of the rectangles would not affect the other, but invoking 
# move_rectangle on either would affect both!
# copy.deepcopy that copies not only the object but also the objects it refers to, and the objects they 
# refer to, and so on. 

#box3 = copy.deepcopy(box)
#print(box3 is box)
#print(box3.corner is box.corner)

# 15.7 Debugging