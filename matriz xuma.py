# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 17:08:07 2014

@author: Toshiron
"""

def suma(m1, m2, m3):
    i=0
    while i<len(m1):
        j=0
        while j<len(m1[0]):
            m3[i][j]=m1[i][j]+m2[i][j]
            #print m3, "lden: ",len(m1), "1:", i
            j+=1
        #print "hola"
        i+=1
    return m3
    
m1=[[2,2,1], [3,2,1], [2,3,2], [2,0,4]]
m2=[[0,1,4], [1,4,0], [2,1,1], [0,2,2]]
m3=[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
suma=suma(m1, m2, m3)
print suma