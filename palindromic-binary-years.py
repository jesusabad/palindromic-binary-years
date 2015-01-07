# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 10:03:01 2015

@author: jesus
"""
print 'Años binariamente palindrómicos'
for num in range(1800,2500):
    cadenabin=bin(num)[2:]
    if cadenabin==cadenabin[::-1]:
        print '%s: %s'%(num,cadenabin)
