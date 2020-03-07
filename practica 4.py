# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 23:56:35 2014

@author: Toshiron
"""

A = int(raw_input("year "))
if A>=1982:
    if A<=2048:
        a = A%19
        b = A%4
        c = A%7
        d = (19*a + 24)%30
        e = (2*b + 4*c + 6*d +5)%7
        n = 22 + d + e
        if n<=31:
            print n, "de marzo"
        else:
            n>=31
            n = n - 31
            print n, "de abril"
    else:
        print "error, el year debe ser menor o igual a 2048"
else:
    print "error, el year debe ser mayor o igual a 1982"
