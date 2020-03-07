# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 13:59:19 2014

@author: Toshiron
"""

temp = int(raw_input("temperatura "))
while temp>=99 or temp<-99:
    print "ingrease bien el dato"
    temp = int(raw_input("temperatura "))
maxima = temp
temp = int(raw_input("temperatura "))
while temp<99 or temp>-99:
    if temp>maxima:
        maxima = temp
        
        temp = int(raw_input("temperatura "))
print "la temperatura maxima es ", maxima, " grados"