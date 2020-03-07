# -*- coding: utf-8 -*-
"""
Created on Thu May 08 15:38:42 2014

@author: Toshiron
"""

h = float(raw_input("altura del edificio: "))
t = 0
g = 9.8
while h >= 0:
    f = h - (g*(t**2))/2
    if f >= 0:
        print "la altura en ", t, " segundos de caida es ", f
    h -= 1
    t += 0.0001