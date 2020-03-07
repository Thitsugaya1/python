# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:43:25 2014

@author: Toshiron
"""

from utalcanvas import *

def columnas_filas():
    window_size(400,500)
    window_coordinates(0,0,400,500)
    create_line(0,400,400,400,"orchid4")
    create_line(0,100,400,100,"orchid4")
    create_line(0,200,400,200,"orchid4")
    create_line(0,300,400,300,"orchid4")
    create_line(100,0,100,400,"orchid4")
    create_line(200,0,200,400,"orchid4")
    create_line(300,0,300,500,"orchid4")
    
show_window()
columnas_filas()