# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 20:54:39 2018

@author: sar_n
"""

def espaciosEnString(cadena):
    space = 0
    i = 0
    while i < len(string):
        if string[i] == " ":
            space += 1
        i += 1
    return space

def spaceInString(string):
    space = 0
    for i in string:
        if i == " ":
            space += 1
    return space

string = raw_input("Ingrese cadena de string: ")
print "la cadena posee", spaceInString(string), "espacios"