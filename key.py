# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 14:19:15 2014

@author: Toshiron
"""

from utalcanvas import *

def movimiento():
    finished = False
    while finished == False:
        key = keypressed(0)
        if key == Key_Left:
            print key
            finished = True
        elif key == Key_Up:
            print key
            finished = True
        elif key == Key_Down:
            print key
            finished = True
        elif key == Key_Right:
            print key
            finished = True
    return key

m = movimiento()
print m