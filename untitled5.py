# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:58:11 2014

@author: Toshiron
"""

def linea(numero):
    while numero > 0:    
        print numero,
        numero -= 2

numero = int(raw_input("numero: "))
while numero > 0:
    linea(numero)
    numero -= 2
    print ""