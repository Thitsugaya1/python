# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 17:45:35 2014

@author: Toshiron
"""

def traspuesta(m1, m2):
    i=0
    t="true"
    while i<len(m1):
        j=0
        while j<len(m1[0]):
            if m1[i][j]==m2[j][i]:
                f=0
                f+=1
            else:
                t="false"
            j+=1
        i+=1
    return t

m1=[["a","b"], ["c","d"]]
m2=[["a","c"], ["b","d"]]
s=traspuesta(m1, m2)
print s