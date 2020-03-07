# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 08:04:01 2014

@author: Toshiron
"""

matriz = []
i = 0
e = 0
m = 4
n = 4
b = []
while e < n:
    while i < m:    
        a = [0]
        b += a
        i += 1
    matriz.append(b)
    e += 1
print matriz
matriz[0][0] = 1
print matriz