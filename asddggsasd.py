from utalcanvas import *
from random import randint

def pause():    
    finished = False
    while finished == False:
        key = keypressed(0)
        if key == Key_P:
            break

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
    
def gato1():
    create_filled_rectangle(0,0,100,100,"orchid4","green")
    #cabeza del gato
    create_filled_circle(50,50,20,"orange")
    #oreja 1
    create_line(30,50,30,70,"orange")
    create_line(30,70,50,50,"orange")
    create_line(30.1,50.1,30.1,70.1,"orange")
    create_line(30.1,70.1,50.1,50.1,"orange")
    #oreja 2
    create_line(70,50,70,70,"orange")
    create_line(70,70,50,50,"orange")
    create_line(69.9,49.9,69.9,69.9,"orange")
    create_line(70.9,69.9,51.9,51.9,"orange")
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

def gato3():
    create_filled_rectangle(200,0,300,100,"orchid4","green")
    #cabeza del gato
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
    #cabeza del gato
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
    
#programa
show_window()
columnas_filas()
o = 0
while o >= 0:
    a = randint(1,4)
    if a == 1:
        gato1()
    elif a == 2:
        gato2()
    elif a == 3:
        gato3()
    elif a == 4:
        gato4()
    o += 1
pause()
        