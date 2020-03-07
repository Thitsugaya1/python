# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 12:43:49 2015

@author: Toshiron
"""

def troll(nombre):
    if nombre == "nikho":
        print "al cesar le gusta el pico xD"
    elif nombre == "cesar":
        print "el cesar es un mapache xD"

print "escriba nikho o cesar"
nombre = raw_input("ingrese nombre: ")
frase = troll(nombre)
