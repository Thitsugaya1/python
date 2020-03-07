# -*- coding: utf-8 -*-
"""
Created on Sun Jun 08 00:19:32 2014

@author: Toshiron
"""

def diagonal_superior(matriz1):
    if len(matriz1)==len(matriz1[0]):
        i=0
        t="true"
        while i<len(matriz1):
            j=0
            while j<len(matriz1[0]):
                if not(matriz1[i][j]!=0 and i==j):
                    t="false"
                j+=1
                i+=1
        j=0
        i=0
        while j<len(matriz1):
            i+=1
            while i<len(matriz1[0]):
                if not(matriz1[i][j]==0 and i>j):
                    t="false"
                i+=1
            j+=1
    else:
        t="false"
    return t

matriz1=[[1,2,4,2,3], [0,3,4,2,5], [0,0,3,2,4], [0,0,0,3,2], [0,0,0,0,1]]
vof=diagonal_superior(matriz1)
print vof