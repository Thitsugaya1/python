# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 20:59:55 2014

@author: Toshiron
"""

from utalcanvas import *

# las columnas

def columnas_filas():
    window_size(400,500)
    window_coordinates(0,0,400,500)
    create_line(0,400,400,400,"orchid4")
    create_line(0,100,400,100,"orchid4")
    create_line(0,200,400,200,"orchid4")
    create_line(0,300,400,300,"orchid4")
    create_line(100,0,100,400,"orchid4")
    create_line(200,0,200,400,"orchid4")
    create_line(300,0,300,400,"orchid4")


#cronometro

def dibujar_tiempo(tiempo):
    window_size(400,500)
    window_coordinates(0,0,400,500)
    window_style("Meow tile","purple1")   
    create_filled_circle(350,450,30,"red")
    create_text(350,450,tiempo,20,"centre",str(tiempo),"white")
    create_filled_circle(200,450,35,"orchid4")
    create_filled_rectangle(300,400,400,500,"orchid4","orchid4")
      
#los gatos
def gato1():
    create_filled_rectangle(0,0,100,100,"green","blue")
    create_filled_circle(25,75,3,"orange")
    create_filled_circle(75,75,3,"orange")
    create_line(45,45,50,50,"red")
    create_line()
    create_line()
    create_line()

#programa princial
#tiempo y columnas
tiempo = 11
show_window()
f = 0
e = "Tiempo"+" Fuera"
while tiempo > 0:
    tiempo = tiempo - 1
    sleep(1)
    dibujar_tiempo(tiempo)
    columnas_filas()    
    create_text(200,450,f,20,"up","black")
columnas_filas()
create_text(200,250,e,20,"centre","black")

#gatos
a = 0
valor = 100000
while a < valor:
    b = randint(1,4)
    