# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:24:46 2019

@author: Falble
"""

# Chapter 16 - Classes and functions
# Now that we know how to create new types, the next step is to write functions that take
# programmer-definied objects as parameters and return them as results. 

# 16.1 Time
# we'll define a class called Time that records the time of the day.

class Time:
    """ Represents the time of day
    
    attributes: hour, minute, second
    """

# we can create a new time object and assign attributes:


def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    # '%.2d'--> prints an integer using at least two digits, including a leading zero if necessary
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

# don't use an if statement 
def is_after(t1,t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

timez = Time()
timez.hour = 11
timez.minute = 59
timez.second = 30

tempo = Time()
tempo.hour = 2
tempo.minute = 11
tempo.second = 58
    
#print_time(timez)
#print_time(tempo)
#print(is_after(tempo,timez))

# 16.2 Pure functions
# we'll write two functions that add time values. They demonstrate two kinds of functions: pure functions and
# modifiers. They also demonstrate a development plan --> PROTOTYPE AND PATCH, which is a way to tackling
# a complex problem by starting with a simple prototype and incrementally dealing with the complications

#def add_time_0(t1,t2):
#    sum = Time()
#    sum.hour = t1.hour + t2.hour
#    sum.minute = t1.minute + t2.minute
#    sum.second = t1.second + t2.minute
#    return sum

# the problem is that the function does not deal with cases where number of seconds or minutes adds up to 
# more than sixty. --> although this function is corrext, it is starting to get big. We'll see shorter alternative.

def add_time_1(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
        
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
        
    return sum 

#start = Time()
#start.hour = int(input('Write the starting hour:'))
#start.minute = int(input('Write the starting minute:'))
#start.second = int(input('And now digit the startning second:'))
#print('\n')
#duration = Time()
#duration.hour = 1
#duration.minute = 35 
#duration.second = 0

#print_time(start)
#print_time(duration)
#done = add_time_1(start,duration)
#print_time(done)
    
# 16.3 Modifiers
# Sometimes is useful doe a function to modify the objects it gets as parameters. In that case, the changes are 
# visible to the caller. Functions that work this way are called MODIFIERS.
# increment, which adds a given number of seconds to a Time object, can be written naturally as a modifier
    
def increment_1(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    if time.minute >= 60:
        time.minutes -= 60
        time.hour += 1
        
# is this function correct? what happends if seconds is much greater than sixty?
# in that case, it is enough to carry once, we have to keep doing until time.second is less than sixty.
# one solution is to replace the if statements with while statements. That would make the function correct,
# but not very efficent. --> write the function without any loops (watch Time1 and Time1_soln)
# anything that can be done with modifiers can also be done with pure functions.
# NB programs that use pure function are faster to develop and less error-prone than programs that use modifiers.
# but modifiers are convenient at times, and functional programs tend to be less efficent. 
# NB is recommend writing pure functions whenever it is reasonable and resort to modifiers only if there is 
# a compelling advantage. ---> FUNCTIONAL PROGRAMMING STYLE

# 16.4 Prototyping vs planning

# when we wrote add_time_1 and increment_1, we were effectively doing addition in base 60, which is why we had to 
# carry from one column to the next.
# --> we can convert Time objects and take advantage of the fact that the computer knows how to do integer arithmetic
# here is a function that converts Times to integers:
        
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

#print(time_to_int(tempo))

# and here is a function that converts an integer to a Time(recall that divmod divides the first argument by 
# second and returns the quotient and remainder as a tuple)

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# convice yourself that it works

#if time_to_int(int_to_time(718)) == 718:
#    print('it works!')
#else:
#    print('sucks')
    
#print_time(int_to_time(7918))
#print(time_to_int(timez))
#print_time(int_to_time(43170))

# once you are convinced they are correct, use them to rewrite add_time_1:

#def add_time(t1,t2):
#    seconds = time_to_int(t1) + time_to_int(t2)
#    return int_to_time(seconds)

#print_time(timez)
#print_time(tempo)
#add = add_time(timez,tempo)
#print_time(add)

# 16.5 Debugging
# a time object is well-formed if the values of minute and second are between 0 and 60 (including 0 but not 60)
# and if hour is positive. hour and minute should be integral values, but we might allow second to have a fraction part.
# writing code to check invariants can help detect errors and find their causes.
    
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0 :
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

# at the beginning of each function you could check the arguments to make sure they are valid. (watch add_time)

#def add_time(t1,t2):
#    if not valid_time(t1) or not valid_time(t2):
#        raise ValueError('invalid Time object in add_time')
#    seconds = time_to_int(t1) + time_to_int(t2)
#    return int_to_time(seconds)

# or you could use an assert statement, which checks a given invariant and raises an exception if it fails
    
def add_time(t1,t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)