# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:58:11 2014

"""

#Enunciado:
#Disene un programa de python que dado un numero, genere una piramide numnerica
#

numero = int(raw_input("numero: "))
while numero <= 0:
    numero = int(raw_input("numero: "))
for i in range (0, numero):
    for j in range (i+1, 0, -1):
        print j,
    print
