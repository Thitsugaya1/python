# -*- coding: utf-8 -*-
"""
Created on Sun Jun 08 00:13:17 2014

@author: Toshiron
"""

def traspuesta(matriz1, matriz2):
    i=0
    t="true"
    while i<len(matriz1):
        j=0
        while j<len(matriz1[0]):
            if not(matriz1[i][j]==matriz2[j][i]):
                t="false"
            j+=1
        i+=1
    return t
    
matriz1=[["a","b"], ["c","d"]]
matriz2=[["a","c"], ["b","d"]]
vof=traspuesta(matriz1, matriz2)
print vof