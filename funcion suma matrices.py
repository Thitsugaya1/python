# -*- coding: utf-8 -*-
"""
Created on Wed May 28 15:50:09 2014

@author: Toshiron
"""

from random import randint

def sumar(matriz):
    i = 0
    suma = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            suma += matriz[i][j]
            
            j += 1
        i += 1
    return suma

n = int(raw_input("filas: "))
m = int(raw_input("columnas: "))
matriz = []
i = 0
while i < n:
    fila = []
    j = 0
    while j < m:
        num = randint(1,20)
        fila += [num]
        j += 1
    matriz += [fila]
    i += 1
print matriz
suma = sumar(matriz)
print "la suma de las variables es:", suma