# -*- coding: utf-8 -*-
"""
Created on Sun Apr 06 13:12:08 2014

@author: Toshiron
"""

Ga = float(raw_input("cantidad de amigos "))
Vc = float(raw_input("valor de la cuenta "))
Tp = (Vc*1.19)*1.1
Vp = Tp/Ga
print "$",Vp, "pesos por persona"

#probar con 5 personas y $10.000 de cuenta, deberia dar 2681 creo
