# -*- coding: utf-8 -*-
"""
Created on Thu May 15 11:37:03 2014

@author: Toshiron
"""

n = int(raw_input("ingrese numero: "))
i = 0
while i <= n:
    n -= i
    print n
    i += 1
        
    while i <= n:
    
        print n,
        i+=1