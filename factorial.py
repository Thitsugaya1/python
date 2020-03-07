# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 19:29:28 2014

@author: Toshiron
"""

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(raw_input("n? "))
f = factorial(n)
print f
#GG para esto :P
