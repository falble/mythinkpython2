# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:17:57 2019

@author: Falble
"""

# Chapter 14 - Files

# 14.1 Persistence
# programs can be persistent: they run for long time (or all the time); they keep at least some of their data
# in permant storage (a hard drive, for example); and if they shut down and restart, they pick up where they left off.
# ex. operating systems. One of the simplest ways for programs to mantain their data is by reading and writing text
# files. an alternative is to store in database and a module, pickle, that makes it easy to store program data.

# 14.2 Reading and writing
# to write a file, you have to open it with mode 'w' as a second parameter:

#fout = open('output.txt','w')
#line1 = "This here's the wattle,\n"
#fout.write(line1)
#line2 = "the emblem of our land.\n"
#fout.write(line2)
#fout.close()

# NB if you don't close the file, it gets closed for you when the programs ends.

# 14.3 Format operator
# the argument of write has to be a string, so if you want to put other values in a file, we have to convert them
# to strings. The easiest way to do that is with str.

#x = 52
#fout.write(str(x))

# an alternative is to use the format operator, %. When applied to integers,% is the modulus operator.
# But when the first operand is a string, % is the format operator.
# The first operand is the format string, which contains one or more format sequences, which specify how the 
# second operand is formatted. The result is a string. ex. '%d' means that the second operand should be
# formatted as a decimal integer

#camels = 42
#print('%d' %camels)
#print('I have spotted %d camels.' %camels)

# if there is more than one format sequence in the string, the second argument has to be a tuple. Each format 
# sequence is matched with an element of the tuple, in order.
# the following example uses '%d' to format an integer, '%g' to format a floating-point number, 
# and '%s' to format a string. NB the number of elements in the tuple has to match the number of format sequences 
# in the string. Also, the types of the elements have to match the format sequences

#print('In %d years I have spotted %g %s.' %(3, 0.1, 'camels'))

# 14.4 Filenames and paths
# the os module provides functions for working with files and directions ('os' stands for operanting system)
# os.getcwd returns the name of the current directory

#import os 

#cwd = os.getcwd()
#print(cwd)

# C:\Users\Utente\Desktop\BOCCONI\3°Anno\PYTHON PROGRAMMING FOR ECONOMICS, MANAGEMENT 
# AND FINANCE\THINKPYTHON2\CAP14-Files  --> identifies a file or directory is called a path.
# memo.txt is also a path but is a relative path. a path that begins with / does not depend on the current directory
# it is called an absulute path

#print(os.path.abspath('output.txt'))
#print(os.path.exists('output.txt'))

# the following example walks through a directory, prints the names of all the files, and calls itself recursively
# on all directories.

#def walk(dirname):
#    for name in os.listdir(dirname):
#        path = os.path.join(dirname, name) # os.path.join takes a directory and a file name and joins them into
#                                           # a complete path.
#        if os.path.isfile(path):
#            print(path)
#        else:
#            walk(path)

# 14.5 Catching exceptions
# a lot of things can go wrong when you try to read and write files. to avoid this errors, you could use
# functions like os.path.exists and os.path.isfile, but it would take a lot of time and code to check
# all the possibilities. it is better to go ahead and try-and deal with problems if they happen-which is 
# exactly what the try statements does. The syntax is similar to an if ... else statements

#try:
#    fin = open('bad_file')
#except:
#    print('Something went wrong')
    
# python starts by executing the try clause. if all goes well, it skips the except clause and proceeds.
# if an exception occurs, it jumps out of the try claise and runs the except clause.
# handling an exception with a try statement is called catching an exception. in this example, the except 
# clause prints an error mex.. in general gives you a chance to fix the problem, or try again

# 14.6 Databases
# the module dbm provides an interface for creating and updating database files. as an ex create a database
# that contains captions for image files. 
# opening a database is similar to opening other files

#import dbm
#db = dbm.open('captions','c')

# NB the mode 'c' means that the database should be created if it doesn't already exist. The result is a database
# object that can be used like a dictionary.

#db['cleese.png'] = 'Photo of john cleese'
#print(db['cleese.png']) # the result is a byte object that is similar to string 

# if you make another assignment to an existing key, dbm replaces the old value:

#db['cleese.png'] = 'photo of stocazzo che te se frega'
#print(db['cleese.png'])

# some dictionary methods, like key and items, dont work with database objects. but iteration with for loop works

#for key in db:
#    print(key,db[key])
#    
#db.close

# 14.7 Pickling 
# a limitation of dbm is that keys and values have to be strings or bytes.
# the pickle module can help. it translates almost any type of object into a string suitable for storage
# in a database, and then translates strings back into objects.
# pickle.dumps takes an object as a parameter and returns a string representation (dump is short for 'dump string')

#import pickle 

#t = [1,2,3]
#print(pickle.dumps(t))  # to read it pickle.loads

#t1 = [1,'due',3]
#s = pickle.dumps(t1)
#t2 = pickle.loads(s)
#print(t2)

# although the new object has the same value as the old, is not (in general) the same object:

#if t1 == t2:
#    print('exception')
#else: 
#    print('ok')
#    
#if t1 is t2:
#    print('exception')
#else: 
#    print('ok')
    
# in other words pickling and then unpickling has the same effect as copying the object.
    
# 14.8 Pipes
# shell = command-line interface. shells usually provide commands to navigate the file system and launch applications.
# any program you can launch from the shell can also be launched from python using a pipe object, which
# represents a running program. 
# [...]

# 14.9 Writing modules
# any files that contains python code can be imported as a module

#import wc

#print(wc)

#print(wc.linecount('thinkpythonCAP14.py'))