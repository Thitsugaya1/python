# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:48:09 2014

@author: Toshiron
"""

x = int(raw_input("x "))
y = int(raw_input("y "))
R1 = int(raw_input("Radio 1 "))
R2 = int(raw_input("Radio 2 "))
R3 = int(raw_input("Radio 3 "))
if  R1>0 and R2>R1 and R3>R2:
    if  x*x + y*y <= R3*R3:
        if  x*x + y*y <= R2*R2:
            if  x*x + y*y <= R1*R1:
                print "ptje = 200"
            else:
                if  x==y:
                    print "ptje = 300"
                else:
                    print "ptje = 150"
        else:
            print "ptje = 100"
    else:
        print "ptje = 0"
else:
    print "error en ingreso de datos"