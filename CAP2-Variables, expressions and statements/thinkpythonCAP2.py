# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:26:06 2019

@author: Utente
"""
#Chapter 2

#compute the percentage of the hour that has elapsed 

message = 'And now for something completely different'
minute = 60 #write the minutes
percentage = (minute * 100) / 60

print(message, percentage,'%')

#exercises

#2.1
#1
n = 42

print(n*2)
#2
x = y = 1

print(2*x,3*y,x*y)

#2.2
#1
r = 5
pi = 3.14
volume = 4/3*r**3*pi

print(volume)
#2
copy = 60
cover_price = 24.95
discount = 0.4 
shipping_cost = 3

total_cost = (copy * cover_price * discount + shipping_cost + 0.75 * copy)

print(total_cost)
#3
first_time = 8 + 15/60
second_time = 7 + 12/60
third_time = 8 + 15/60

total_time = (first_time + 3*second_time + third_time)

print(total_time,'minutes')


