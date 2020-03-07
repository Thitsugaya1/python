# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:10:26 2014

@author: Toshiron
"""

n = int(raw_input("numero: "))
s = 0
v = 0
while s<n:
    if v % 2 == 0:
        s = s + 2
        print s
    else:
        s = s + 3
        print s
    v = v + 1
print v, "vueltas"