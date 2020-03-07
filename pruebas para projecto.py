# -*- coding: utf-8 -*-
"""
Created on Thu May 01 14:46:18 2014

@author: Toshiron
"""

from random import randint
from utalcanvas import *

def dibujar_tiempo(tiempo):
    erase()
    window_size(700,750)
    window_coordinates(0,0,800,800)
    window_style("Meow tile","purple1")
    create_filled_circle(750,750,30,"red")
    create_text(750,750,tiempo,20,"centre",str(tiempo),"white") 
    create_line(0,200,800,200,"orchid4")
    create_line(0,400,800,400,"orchid4")
    create_line(0,600,800,600,"orchid4")
    create_line(200,0,200,800,"orchid4")
    create_line(400,0,400,800,"orchid4")
    create_line(600,0,600,800,"orchid4")
    create_filled_circle(400,750,35,"orchid4")
    
def dibuja_gato():
    erase()
    gato1 = randint(1,4)
    dibujar_gato1(1,gato1)
    gato2 = randint(1,4)
    dibujar_gato2(2,gato2)
    gato3 = randint(1,4)
    dibujar_gato3(3,gato3)
    gato4 = randint(1,4)
    dibujar_gato4(4,gato4)
    
def crear_gato(dibuja_gato):
    create_filled_circle()
    
    
tiempo = 11
show_window()
f = 0
none = "1" or "2" or "3" or "6" or "9"
d = "game " + "over"
e = "Tiempo"+" Fuera"
while tiempo > 0:
    tiempo = tiempo - 1
    sleep(1)
    dibujar_tiempo(tiempo)
    create_text(400,750,f,30,"up","black")
    sleep(0.001)
    while h != none or h != none or h != none or h != none:
        if gato1 == 1 or gato1 == 2 or gato1 == 3 or gato1 == 4:
            f += 1
            if f%50 == 0:
                tiempo = 10 + tiempo
        else:
            create_text(400,600,d,30,"black")
            sleep(2)
            close_window()
    create_text(400,600,d,30,"black")
    sleep(2)
    close_window()
create_text(400,400,e,30,"centre","black")
sleep(2)
close_window()