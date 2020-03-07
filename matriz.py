# -*- coding: utf-8 -*-
"""
Created on Wed May 28 14:29:07 2014

@author: Toshiron
"""

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

n = int(raw_input("numero de filas: "))
m = int(raw_input("numero de columnas: "))
matriz = []
i = 0
while i < n:
    fila = []
    j = 0
    while j < m:
        num = int(raw_input("numero: "))
        fila += [num]
        j += 1
    matriz += [fila]
    print ""
    i += 1