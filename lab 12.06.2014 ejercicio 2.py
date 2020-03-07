# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 16:35:00 2014

@author: Toshiron
"""

from random import randint

def rana(m, f, c):
    i=0
    n=0
    x=0
    y=0
    while i <= n:
        j = randint(0,3)
        if j == 0:
            #arriba
            if (x-1) >= 0:
                m[x-1][y] = 1
                x -= 1
                i += 1        
        if j == 1:
            #derecha
            if (y+1) <= f:
                m[x][y+1] = 1
                y += 1
                i += 1
        if j == 2:
            #abajo
            if (x+1) <= c:
                m[x+1][y] = 1
                x += 1
                i += 1
        if j == 3:
            #izquierda
            if (y-1) >= 0:
                m[x][y-1] = 1
                y -= 1
                i += 1
    return m
    
f=int(raw_input("filas: "))
c=int(raw_input("columnas: "))
m=[]
q=0
while q < f:
    fila=[0]*f
    m=[fila]
    q+=1
matriz=rana(m, f, c)
print matriz