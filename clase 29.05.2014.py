# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:42:20 2014

@author: Toshiron
"""

def sort2(lista):
    inicio = 0
    j = 1
    n = len(lista)
    nueva = []
    while inicio < n:
        r = 0
        while inicio<len(lista) and lista[inicio] != j:
            inicio += 1
            r += 1
        nueva += [j]
        #if inicio<len(lista):
         #   del(lista[inicio])
        inicio -= r
        inicio += 1
        j += 1
    return nueva
    
lista = [2,4,1,5,3,6,7,11,13,8,10,9,12]
print lista
s = sort2(lista)
lista.sort()
print s
print lista