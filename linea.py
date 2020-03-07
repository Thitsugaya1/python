# -*- coding: utf-8 -*-
"""
Created on Wed May 07 17:58:33 2014

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
    create_line(300,0,300,400,"orchid4")
    
def dibujar_tiempo(tiempo):
    erase()
    window_size(400,500)
    window_coordinates(0,0,400,500)
    window_style("Meow tile","purple1")   
    create_filled_circle(350,450,30,"red")
    create_text(350,450,tiempo,20,"centre",str(tiempo),"white")
    create_filled_circle(200,450,35,"orchid4")

#los gatos
def gato1():
    create_filled_rectangle(0,0,100,100,"orchid4","green")
    create_filled_circle(50,50,20,"orange")
    #oreja 1
    create_line(30,50,30,70,"orange")
    create_line(30,70,50,50,"orange")
    create_line(31,51,31,71,"orange")
    create_line(30,71,49,49,"orange")
    #oreja 2
    create_line(70,50,70,70,"orange")
    create_line(70,70,50,50,"orange")
    create_line(69,49,69,69,"orange")
    create_line(70,69,51,51,"orange")
    #lente ojo izquierdo
    create_filled_circle(41,56,5,"black")
    #lente ojo izquierdo
    create_filled_circle(59,56,5,"black")
    #marco del lente    
    create_line(41,56,59,56,"black")
    #boca
    create_circle(45,43,5,"black")
    create_circle(55,43,5,"black")
    create_filled_rectangle(45,43,55,48,"orange")
    
def gato2():
    create_filled_rectangle(100,0,200,100,"orchid4","green")
    create_filled_circle(150,50,20,"orange")
    #oreja 1
    create_line(130,50,130,70,"orange")
    create_line(130,70,150,50,"orange")
    create_line(131,51,131,71,"orange")
    create_line(130,71,149,49,"orange")
    #oreja 2
    create_line(170,50,170,70,"orange")
    create_line(170,70,150,50,"orange")
    create_line(169,49,169,69,"orange")
    create_line(170,69,151,51,"orange")
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

def gato3():
    create_filled_rectangle(200,0,300,100,"orchid4","green")
    create_filled_circle(250,50,20,"orange")
    #oreja 1
    create_line(230,50,230,70,"orange")
    create_line(230,70,250,50,"orange")
    create_line(231,51,231,71,"orange")
    create_line(230,71,249,49,"orange")
    #oreja 2
    create_line(270,50,270,70,"orange")
    create_line(270,70,250,50,"orange")
    create_line(269,49,269,69,"orange")
    create_line(270,69,251,51,"orange")
    #lente ojo izquierdo
    create_filled_circle(241,56,5,"black")
    #lente ojo izquierdo
    create_filled_circle(259,56,5,"black")
    #marco del lente    
    create_line(241,56,259,56,"black")
    #boca
    create_circle(245,43,5,"black")
    create_circle(255,43,5,"black")
    create_filled_rectangle(245,43,255,48,"orange")
    
def gato4():
    create_filled_rectangle(300,0,400,100,"orchid4","green")
    create_filled_circle(350,50,20,"orange")
    #oreja 1
    create_line(330,50,330,70,"orange")
    create_line(330,70,350,50,"orange")
    create_line(331,51,331,71,"orange")
    create_line(330,71,349,49,"orange")
    #oreja 2
    create_line(370,50,370,70,"orange")
    create_line(370,70,350,50,"orange")
    create_line(369,49,369,69,"orange")
    create_line(370,69,351,51,"orange")
    #lente ojo izquierdo
    create_filled_circle(341,56,5,"black")
    #lente ojo izquierdo
    create_filled_circle(359,56,5,"black")
    #marco del lente    
    create_line(341,56,359,56,"black")
    #boca
    create_circle(345,43,5,"black")
    create_circle(355,43,5,"black")
    create_filled_rectangle(345,43,355,48,"orange")

def gato5():
    create_filled_rectangle(0,100,100,200,"orchid4","green")
    create_filled_circle(50,150,20,"orange")
    #oreja 1
    create_line(30,150,30,170,"orange")
    create_line(30,170,50,150,"orange")
    create_line(31,151,31,171,"orange")
    create_line(30,171,49,149,"orange")
    #oreja 2
    create_line(70,150,70,170,"orange")
    create_line(70,170,50,150,"orange")
    create_line(69,149,69,169,"orange")
    create_line(70,169,51,151,"orange")
    #lente ojo izquierdo
    create_filled_circle(41,156,5,"black")
    #lente ojo izquierdo
    create_filled_circle(59,156,5,"black")
    #marco del lente    
    create_line(41,156,59,156,"black")
    #boca
    create_circle(45,143,5,"black")
    create_circle(55,143,5,"black")
    create_filled_rectangle(45,143,55,148,"orange")
    
def gato6():
    create_filled_rectangle(100,100,200,200,"orchid4","green")
    create_filled_circle(150,150,20,"orange")
    #oreja 1
    create_line(130,150,130,170,"orange")
    create_line(130,170,150,150,"orange")
    create_line(131,151,131,171,"orange")
    create_line(130,171,149,149,"orange")
    #oreja 2
    create_line(170,150,170,170,"orange")
    create_line(170,170,150,150,"orange")
    create_line(169,149,169,169,"orange")
    create_line(170,169,151,151,"orange")
    #lente ojo izquierdo
    create_filled_circle(141,156,5,"black")
    #lente ojo izquierdo
    create_filled_circle(159,156,5,"black")
    #marco del lente    
    create_line(141,156,159,156,"black")
    #boca
    create_circle(145,143,5,"black")
    create_circle(155,143,5,"black")
    create_filled_rectangle(145,143,155,148,"orange")
    
def gato7():
    create_filled_rectangle(200,100,300,200,"orchid4","green")
    create_filled_circle(250,150,20,"orange")
    #oreja 1
    create_line(230,150,230,170,"orange")
    create_line(230,170,250,150,"orange")
    create_line(231,151,231,171,"orange")
    create_line(230,171,249,149,"orange")
    #oreja 2
    create_line(270,150,270,170,"orange")
    create_line(270,170,250,150,"orange")
    create_line(269,149,269,169,"orange")
    create_line(270,169,251,151,"orange")
    #lente ojo izquierdo
    create_filled_circle(241,156,5,"black")
    #lente ojo izquierdo
    create_filled_circle(259,156,5,"black")
    #marco del lente    
    create_line(241,156,259,156,"black")
    #boca
    create_circle(245,143,5,"black")
    create_circle(255,143,5,"black")
    create_filled_rectangle(245,143,255,148,"orange")
    
def gato8():
    create_filled_rectangle(300,100,400,200,"orchid4","green")
    create_filled_circle(350,150,20,"orange")
    #oreja 1
    create_line(330,150,330,170,"orange")
    create_line(330,170,350,150,"orange")
    create_line(331,151,331,171,"orange")
    create_line(330,171,349,149,"orange")
    #oreja 2
    create_line(370,150,370,170,"orange")
    create_line(370,170,350,150,"orange")
    create_line(369,149,369,169,"orange")
    create_line(370,169,351,151,"orange")
    #lente ojo izquierdo
    create_filled_circle(341,156,5,"black")
    #lente ojo izquierdo
    create_filled_circle(359,156,5,"black")
    #marco del lente    
    create_line(341,156,359,156,"black")
    #boca
    create_circle(345,143,5,"black")
    create_circle(355,143,5,"black")
    create_filled_rectangle(345,143,355,148,"orange")

def gato9():
    create_filled_rectangle(0,200,100,300,"orchid4","green")
    create_filled_circle(50,250,20,"orange")
    #oreja 1
    create_line(30,250,30,270,"orange")
    create_line(30,270,50,250,"orange")
    create_line(31,251,31,271,"orange")
    create_line(30,271,49,249,"orange")
    #oreja 2
    create_line(70,250,70,270,"orange")
    create_line(70,270,50,250,"orange")
    create_line(69,249,69,269,"orange")
    create_line(70,269,51,251,"orange")
    #lente ojo izquierdo
    create_filled_circle(41,256,5,"black")
    #lente ojo izquierdo
    create_filled_circle(59,256,5,"black")
    #marco del lente    
    create_line(41,256,59,256,"black")
    #boca
    create_circle(45,243,5,"black")
    create_circle(55,243,5,"black")
    create_filled_rectangle(45,243,55,248,"orange")

def gato10():
    create_filled_rectangle(100,200,200,300,"orchid4","green")
    create_filled_circle(150,250,20,"orange")
    #oreja 1
    create_line(130,250,130,270,"orange")
    create_line(130,270,150,250,"orange")
    create_line(131,251,131,271,"orange")
    create_line(130,271,149,249,"orange")
    #oreja 2
    create_line(170,250,170,270,"orange")
    create_line(170,270,150,250,"orange")
    create_line(169,249,169,269,"orange")
    create_line(170,269,151,251,"orange")
    #lente ojo izquierdo
    create_filled_circle(141,256,5,"black")
    #lente ojo izquierdo
    create_filled_circle(159,256,5,"black")
    #marco del lente    
    create_line(141,256,159,256,"black")
    #boca
    create_circle(145,243,5,"black")
    create_circle(155,243,5,"black")
    create_filled_rectangle(145,243,155,248,"orange")

def gato11():
    create_filled_rectangle(200,200,300,300,"orchid4","green")
    create_filled_circle(250,250,20,"orange")
    #oreja 1
    create_line(230,250,230,270,"orange")
    create_line(230,270,250,250,"orange")
    create_line(231,251,231,271,"orange")
    create_line(230,271,249,249,"orange")
    #oreja 2
    create_line(270,250,270,270,"orange")
    create_line(270,270,250,250,"orange")
    create_line(269,249,269,269,"orange")
    create_line(270,269,251,251,"orange")
    #lente ojo izquierdo
    create_filled_circle(241,256,5,"black")
    #lente ojo izquierdo
    create_filled_circle(259,256,5,"black")
    #marco del lente    
    create_line(241,256,259,256,"black")
    #boca
    create_circle(245,243,5,"black")
    create_circle(255,243,5,"black")
    create_filled_rectangle(245,243,255,248,"orange")

def gato12():
    create_filled_rectangle(300,200,400,300,"orchid4","green")
    create_filled_circle(350,250,20,"orange")
    #oreja 1
    create_line(330,250,330,270,"orange")
    create_line(330,270,350,250,"orange")
    create_line(331,251,331,271,"orange")
    create_line(330,271,349,249,"orange")
    #oreja 2
    create_line(370,250,370,270,"orange")
    create_line(370,270,350,250,"orange")
    create_line(369,249,369,269,"orange")
    create_line(370,269,351,251,"orange")
    #lente ojo izquierdo
    create_filled_circle(341,256,5,"black")
    #lente ojo izquierdo
    create_filled_circle(359,256,5,"black")
    #marco del lente    
    create_line(341,256,359,256,"black")
    #boca
    create_circle(345,243,5,"black")
    create_circle(355,243,5,"black")
    create_filled_rectangle(345,243,355,248,"orange")

def gato13():
    create_filled_rectangle(0,300,100,400,"orchid4","green")
    create_filled_circle(50,350,20,"orange")
    #oreja 1
    create_line(30,350,30,370,"orange")
    create_line(30,370,50,350,"orange")
    create_line(31,351,31,371,"orange")
    create_line(30,371,49,349,"orange")
    #oreja 2
    create_line(70,350,70,370,"orange")
    create_line(70,370,50,350,"orange")
    create_line(69,349,69,369,"orange")
    create_line(70,369,51,351,"orange")
    #lente ojo izquierdo
    create_filled_circle(41,356,5,"black")
    #lente ojo izquierdo
    create_filled_circle(59,356,5,"black")
    #marco del lente    
    create_line(41,356,59,356,"black")
    #boca
    create_circle(45,343,5,"black")
    create_circle(55,343,5,"black")
    create_filled_rectangle(45,343,55,348,"orange")
    #boca
    create_circle(45,343,5,"black")
    create_circle(55,343,5,"black")
    create_filled_rectangle(45,343,55,348,"orange")

def gato14():
    create_filled_rectangle(100,300,200,400,"orchid4","green")
    create_filled_circle(150,350,20,"orange")
    #oreja 1
    create_line(130,350,130,370,"orange")
    create_line(130,370,150,350,"orange")
    create_line(131,351,131,371,"orange")
    create_line(130,371,149,349,"orange")
    #oreja 2
    create_line(170,350,170,370,"orange")
    create_line(170,370,150,350,"orange")
    create_line(169,349,169,369,"orange")
    create_line(170,369,151,351,"orange")
    #lente ojo izquierdo
    create_filled_circle(141,356,5,"black")
    #lente ojo izquierdo
    create_filled_circle(159,356,5,"black")
    #marco del lente    
    create_line(141,356,159,356,"black")
    #boca
    create_circle(145,343,5,"black")
    create_circle(155,343,5,"black")
    create_filled_rectangle(145,343,155,348,"orange")
    #boca
    create_circle(145,343,5,"black")
    create_circle(155,343,5,"black")
    create_filled_rectangle(145,343,155,348,"orange")

def gato15():
    create_filled_rectangle(200,300,300,400,"orchid4","green")
    create_filled_circle(250,350,20,"orange")
    #oreja 1
    create_line(230,350,230,370,"orange")
    create_line(230,370,250,350,"orange")
    create_line(231,351,231,371,"orange")
    create_line(230,371,249,349,"orange")
    #oreja 2
    create_line(270,350,270,370,"orange")
    create_line(270,370,250,350,"orange")
    create_line(269,349,269,369,"orange")
    create_line(270,369,251,351,"orange")
    #lente ojo izquierdo
    create_filled_circle(241,356,5,"black")
    #lente ojo izquierdo
    create_filled_circle(259,356,5,"black")
    #marco del lente    
    create_line(241,356,259,356,"black")
    #boca
    create_circle(245,343,5,"black")
    create_circle(255,343,5,"black")
    create_filled_rectangle(245,343,255,348,"orange")
    #boca
    create_circle(245,343,5,"black")
    create_circle(255,343,5,"black")
    create_filled_rectangle(245,343,255,348,"orange")

def gato16():
    create_filled_rectangle(300,300,400,400,"black","green")
    create_filled_circle(350,350,20,"orange")
    #oreja 1
    create_line(330,350,330,370,"orange")
    create_line(330,370,350,350,"orange")
    create_line(331,351,331,371,"orange")
    create_line(330,371,349,349,"orange")
    #oreja 2
    create_line(370,350,370,370,"orange")
    create_line(370,370,350,350,"orange")
    create_line(369,349,369,369,"orange")
    create_line(370,369,351,351,"orange")
    #lente ojo izquierdo
    create_filled_circle(341,356,5,"black")
    #lente ojo izquierdo
    create_filled_circle(359,356,5,"black")
    #marco del lente    
    create_line(341,356,359,356,"black")


#pincipal programa   
tiempo = 10 
show_window()
dibujar_tiempo(tiempo)
columnas_filas()
gato1()
gato2()
gato3()
gato4()
gato5()
gato6()
gato7()
gato8()
gato9()
gato10()
gato11()
gato12()
gato13()
gato14()
gato15()
gato16()
