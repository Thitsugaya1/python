# -*- coding: utf-8 -*-
"""
Created on Wed May 07 15:14:29 2014

@author: Toshiron
"""

tiempo = 51
f = 0
while tiempo > 0:
    tiempo = tiempo - 1
    f +=1
    print f
    if f%50 == 0:
        tiempo = 10 + tiempo