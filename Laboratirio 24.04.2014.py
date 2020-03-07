# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:16:11 2014

@author: Toshiron
"""

from utalcanvas import *

D = raw_input("circulo o rectangulo: ")
if D == "circulo":
    show_window()
    window_coordinates(0,0,10,10)
    print "ingrese valores del 1 al 9, puede ingresar estos valores"
    x = float(raw_input("x: "))
    y = float(raw_input("y: "))
    Radio = float(raw_input("radio: "))
    create_circle(x, y, Radio,"black")
elif D == "rectangulo":
    show_window()
    window_coordinates(0,0,10,10)
    print "ingrese valores del 1 al 9, puede ingresar estos valores"
    v1 = float(raw_input("v1: "))
    v2 = float(raw_input("v2: "))
    t1 = float(raw_input("t1: "))
    t2 = float(raw_input("t2: "))
    create_rectangle(v1,v2,t1,t2)
        
    
