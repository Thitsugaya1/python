# -*- coding: utf-8 -*-
"""
Created on Wed May 07 18:12:15 2014

@author: Toshiron
"""

from random import randint

print "valor entre 0 y 9"
n = int(raw_input("numero: "))
i = 0
while n <= 9 and i == 0:
    while i == 0:
        a = randint(0,9)
        if a == 0:
            print "ganaste"
        elif a == 1:
            print "ganaste"
        elif a == 2:
            print "ganaste"
        elif a == 3:
            print "ganaste"
        elif a == 4:
            print "ganaste"
        elif a == 5:
            print "ganaste"
        elif a == 6:
            print "ganaste"
        elif a == 7:
            print "ganaste"
        elif a == 8:
            print "ganaste"
        elif a == 9:
            print "ganaste"
else:
    print "perdiste"