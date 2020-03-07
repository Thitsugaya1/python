# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 12:43:49 2015

@author: Toshiron
"""

def troll(numero):
    if numero == 0:
        print "al cesar le gusta el pico xD"
    elif numero == 1:
        print "el cesar es un mapache xD"
    elif numero == 2:
        print "anda a predicar mapache #%$&"
    elif numero == 3:
        print "mapache anda a ver eva luna"
    elif numero == 4:
        print "catito quiere pan, xD"
    elif numero != 0 and numero != 1 and numero != 2 and numero != 3 and numero != 4:
        print "escribe numeros entre el 0 y el 4 mapache %&%$&$%"
    
print "escriba numeros entre el 0 y 4"
numero = int(raw_input("ingrese numero: "))
frase = troll(numero)
