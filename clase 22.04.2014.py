# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:23:31 2014

@author: Toshiron
"""

n = int(raw_input("numero: "))
i = 0
while n>1:
    i += 1
    print n
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1
print n
print "itero ",i, " veces"