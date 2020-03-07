# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:45:58 2014

@author: Toshiron
"""

from random import randint

def genera_carta():
    suma = 0
    total = 3
    while total > 0:
        num = randint(1,13)
        if num == 1:
            num = 20
        elif num >= 11 and num <= 13:
            num = 10
        if not(num%4 == 0 or num%4 == 0):
            total -= 1
        suma = suma + num
    return suma
    
#programa principal
suma = genera_carta()
print "la suma que obtuvo es", suma