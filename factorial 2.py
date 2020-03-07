# -*- coding: utf-8 -*-
"""
Created on Sun May 04 20:45:19 2014

@author: Toshiron
"""

#funcion que calcula el factorial de un número 
#entrada: número 
#salida: factorial del número 
def factorial(n): 
    f=1 
    i=1 
    while i<=n: 
        f=f*i 
        i+=1 
    return f 
 
#programa principal 
valor = int(raw_input('ingrese valor: ')) 
Resultado = factorial(valor) 
print Resultado 
