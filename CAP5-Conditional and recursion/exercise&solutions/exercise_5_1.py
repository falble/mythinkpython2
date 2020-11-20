# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:06:16 2019

@author: Utente
"""

#Chapter 5 
#Exercise 5.1

#now and 1 january 1970
import time

print('Seconds=', time.time())
print('Minutes=', time.time()/60)
print('Hours=', time.time()/(60**2))
print('Days=', time.time()//(60**2*24))
print('Years', time.time()//(60**2*24*365))
