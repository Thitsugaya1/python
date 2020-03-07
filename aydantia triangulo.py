# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:58:11 2014

@author: Toshiron
"""

#def linea(numero):
 #   while numero >= 1:    
  #      print numero,
   #     numero -= 1

numero = int(raw_input("numero: "))
while numero <= 0:
    numero = int(raw_input("numero: "))
while numero >= 1:
    i = numero
    while i >= 1:    
        print i,
        i -= 1
    numero -= 1
    print ""


numero = int(raw_input("numero: "))
while numero <= 0:
    numero = int(raw_input("numero: "))
for i in range (1, numero+1):
    for j in range (i, numero +1):
        print i,
    print


numero = int(raw_input("numero: "))
while numero <= 0:
    numero = int(raw_input("numero: "))
for i in range (1, numero+1):
    for j in range (1, i+1):
        print i,
    print

numero = int(raw_input("numero: "))
while numero <= 0:
    numero = int(raw_input("numero: "))
for i in range (0, numero):
    for j in range (i+1, 0, -1):
        print j,
    print
while numero >= 1:
    i = numero - 1
    while i >= 1:    
        print i,
        i -= 1
    numero -= 1
    print ""
