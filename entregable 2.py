# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:13:01 2014

@author: Toshiron
"""

x = int(raw_input("x "))
y = int(raw_input("y "))
R1 = int(raw_input("Radio 1 "))
R2 = int(raw_input("Radio 2 "))
R3 = int(raw_input("Radio 3 "))
if  x*x + y*y <= R1*R1:
    if  x*x + y*y == R1*R1:
        ptje = (150 + 200)/2
    else:
        print "ptje = 200"
else:
    if  x*x + y*y <= R2*R2:
        if  x*x + y*y == R2*R2:
            ptje = (150 + 100)/2
        else:
            print "ptje = 150"
    else:
        if  x*x + y*y <= R3*R3:
            if  x*x + y*y == R3*R3:
                ptje = 100
            else:
                ptje = 100
        else:
            ptje = 0

if x==y or x==-y:
    ptje = ptje*2

print "ptje = ", ptje