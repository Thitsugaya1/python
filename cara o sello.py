# -*- coding: utf-8 -*-
"""
Created on Sun May 04 20:35:44 2014

@author: Toshiron
"""

from random import randint 
 
#programa principal 
i=1
icap = float(raw_input("Ingrese ICAP para hoy: "))
while i < 30: 
    a = randint(1,10)  
    if a == 5 or a == 7:
        b =icap/2
        print "dia",i, "lluvia!" , b 
    else:
        b=(icap*0.1)+icap
        print "dia",i, b 
    i+=1 
    icap=b

