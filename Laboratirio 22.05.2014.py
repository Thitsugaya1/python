# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:35:31 2014

@author: Toshiron
"""

from random import randint

n = int(raw_input("largo de la lista: "))
i = 0
lista = []
while i < n:
    a = randint(0,20)
    lista += [a]
    i += 1
print lista