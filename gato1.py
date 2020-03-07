# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:12:01 2014

@author: Toshiron
"""

from utalcanvas import *

def gato1():
    create_filled_rectangle(100,0,200,100,"orchid4","green")
    #cabeza del gato
    create_filled_circle(150,50,20,"orange")
    #oreja 1
    create_line(130,50,130,70,"orange")
    create_line(130,70,150,50,"orange")
    create_line(130.1,50.1,130.1,70.1,"orange")
    create_line(130.1,70.1,150.1,50.1,"orange")
    #oreja 2
    create_line(170,50,170,70,"orange")
    create_line(170,70,150,50,"orange")
    create_line(169.9,49.9,169.9,69.9,"orange")
    create_line(169.9,69.9,149.9,49.9,"orange")
    #lente ojo izquierdo
    create_filled_circle(141,56,5,"black")
    #lente ojo izquierdo
    create_filled_circle(159,56,5,"black")
    #marco del lente    
    create_line(141,56,159,56,"black")
    #boca
    create_circle(145,43,5,"black")
    create_circle(155,43,5,"black")
    create_filled_rectangle(145,43,155,48,"orange")
    
show_window()
window_size(100,200)
window_coordinates(0,0,100,200)
gato1()