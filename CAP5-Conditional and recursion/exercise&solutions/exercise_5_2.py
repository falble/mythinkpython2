# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:57:35 2019

@author: Utente
"""

#Chapter 5
#Exercise 5.2

#Fermat's last theorem


def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


def check_numbers():
    a = int(input('Choose a fucking number for a= '))
    b = int(input('I choose your mother you choose b= '))
    c = int(input('Piatek scores and c? '))
    n = int(input("I'm watching you, but i don't know n, n is? "))
    
    return check_fermat(a, b, c, n)

check_numbers()  