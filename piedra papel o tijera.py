# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:56:14 2016

@author: Toshiron
"""

from random import randint
j=0
p=0
for i in range(3):
    n=int(raw_input("ingrese 1 (tigera), 2 (piedra) o 3(papel)"))
    a=randint(1,3)
    print "el jugador escoguio:"
    if n == 1:
        print "tigera"
    elif n == 2:
        print "piedra"
    else:
        print "papel"
        print "Python escoguio:"
    if a == 1:
        	print "tigera"
    elif a == 2:
        	print "piedra"
    else:
        	print "papel"
    if n == a:
        	print "empate"
    elif (n == 1 and a == 2) or (n== 3 and a == 1) or (n == 2 and a == 3):
        	print "gana Python"
         p+=1
    elif (n == 2 and a == 1) or (n== 1 and a == 2) or (n == 1 and a == 2):
        	print "gana jugador"
         j+=1
if j == p:
	print "juego terminado tenemos un empate"
elif j > p:
	print "juego terminado gana jugador"
else:
	print "juego terminado gana Python"