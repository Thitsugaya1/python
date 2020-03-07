# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:33:09 2016

@author: Toshiron
"""

from random import randint
num = int(raw_input(": "))
matriz = []
for i in range (0,num):
    fila = []
    for j in range (0,num):
        fila += [randint(1,10)]
    matriz += [fila]
for i in range (0,num):
    print matriz[i]