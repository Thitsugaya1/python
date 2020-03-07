# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Toshiron\.spyder2\.temp.py
"""

NEM = float(raw_input("Nem "))
Ran = float(raw_input("Ranking "))
Leng = float(raw_input("Lenguaje "))
Mate = float(raw_input("Matematicas "))
Cien = float(raw_input("Ciencias "))
Vn = NEM*25/100
Vr = Ran*25/100
Vl = Leng*10/100
Vm = Mate*30/100
Vc = Cien*10/100
Vt = ( Vn + Vr + Vl + Vm + Vc )
print Vt