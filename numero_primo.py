# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 16:51:55 2018

@author: sar_n
"""

#One way to solve
number = int(raw_input("Set a number: "))
i = 1
print "1 Is a 'numero primo'"
while i <= number: 
    j = 1    
    primo = 0
    while j <= i:
        if i%j == 0:
            primo+=1
        j+=1
    if primo == 2:
        print i, "Is a 'numero primo'"
    i += 1
print ""
#Another way
for i in range (1, number+1): 
    primo = True
    for j in range (2,i):
        if i%j == 0:
            primo = False
            break
    if primo:
        print i, "Is a 'numero primo'"
