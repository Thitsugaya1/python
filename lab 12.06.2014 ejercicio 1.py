# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 15:49:09 2014

@author: Toshiron
"""

from random import randint

def generar_tablero(nivel):
    i = 0
    x=3
    y=3
    m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    while i < nivel:
        j = randint(0,3)
        if j == 0:
            #arriba
            if (x-1) >= 0:
                m[x][y] = m[x-1][y]
                m[x-1][y] = 0
                x -= 1
                i += 1        
        if j == 1:
            #derecha
            if (y+1) <= 3:
                m[x][y] = m[x][y+1]
                m[x][y+1] = 0
                y += 1
                i += 1
        if j == 2:
            #abajo
            if (x+1) <= 3:
                m[x][y] = m[x+1][y]
                m[x+1][y] = 0
                x += 1
                i += 1
        if j == 3:
            #izquierda
            if (y-1) >= 0:
                m[x][y] = m[x][y-1]
                m[x][y-1] = 0
                y -= 1
                i += 1
    return m

#Programa Principal
nivel = float(raw_input("Ingrese Nivel: "))
tablero = generar_tablero(nivel)
print tablero

