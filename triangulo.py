# -*- coding: utf-8 -*-
"""
Created on Thu May 15 11:29:44 2014

@author: Toshiron
"""

def linea(numero):
    while numero > 0:    
        print numero,
        numero -= 1

numero = int(raw_input("numero: "))
while numero > 0:
    linea(numero)
    numero -= 1
    print ""
