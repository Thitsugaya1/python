# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:35:31 2014

@author: Toshiron
"""

from random import randint

def lista_hecha():
    i = 0
    lista = []
    while i < n:
        lista += [randint(0,20)]
        i += 1
    return lista

n = int(raw_input("largo de la lista: "))
lista = lista_hecha()
print lista