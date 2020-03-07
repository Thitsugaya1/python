# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:57:59 2014

@author: Toshiron
""" 
            
lista = [0,3,6,9,12,15,18,21,24,27,30,33,36,39]
lista.sort()
print lista
m = int(raw_input("valor que quere encontrar: "))
inicio = 0
fin = len(lista) - 1
largo = len(lista)
i = len(lista)/2
while m != lista[i]:
    if lista[i] > m:
        fin = i - 1
        largo = fin - inicio + 1
        i = (largo/2) + inicio
    else:
        inicio = i
        largo = fin - inicio + 1
        i = (largo/2) + inicio
if lista[i] == m:
    print "se encontro, :3"
else:
    print "no esta en esta lista, intentalo de nuevo :/"