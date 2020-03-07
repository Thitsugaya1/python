# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:38:02 2014

@author: Toshiron
"""
from utalcanvas import *

def crea_lineas(n):
    p = "1"
    i = 0
    while i < (n-1):
        p = p + str(i+2)
        i += 1        
        print p

n = int(raw_input("n: "))
p = "1"
print p
crea_lineas(n)
