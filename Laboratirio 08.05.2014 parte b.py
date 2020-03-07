# -*- coding: utf-8 -*-
"""
Created on Thu May 08 15:38:42 2014

@author: Toshiron
"""
from utalcanvas import *

def dibujar_caida(f):
    erase("c1")
    window_size(40,30)
    x1 = 10
    y1 = f
    window_coordinates(0,0,40,30)
    create_filled_rectangle(0,0,9,h)
    create_filled_circle(x1,y1,1,"black","orchid4","c1")
    sleep(1)
    
def congelar(z):
    x
    
#programa principal
h = float(raw_input("altura del edificio: "))
t = 0
z = float(raw_input("momento a congelarse: "))
g = 9.8
show_window()
while h >= 0:
    f = h - (g*(t**2))/2
    if f >= 0:
        print "la altura en ", t, " segundos de caida es ", f
    dibujar_caida(f)
    h -= 1
    t += 0.0001