# -*- coding: utf-8 -*-
"""
Created on Tue Apr 01 19:47:47 2014

@author: Toshiron
"""

Cantidad_horas = float(raw_input("cantidad de horas: "))
Cantidad_anios = float(raw_input("Edad: "))
Total_Horas = Cantidad_anios*8760
Hd = 24/Cantidad_horas
Ho_dormidas = Total_Horas/Hd
Di_dormidos = Ho_dormidas/24
Year_d = Di_dormidos/365
print Year_d, "anios que ah dormido en su vida"
