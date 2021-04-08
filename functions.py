# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:03:49 2020

@author: vignesh jaishankar
"""

def addOne(number):
    output= number +1
    return output
var=0
print(var)
var2= addOne(var)
var3= addOne(var2)
var4= addOne(2.1 + 3.4)

print(var2)
print(var3)
print(var4)

def addOneAddTwo(numberOne,numberTwo):
    output = numberOne + 1
    output += numberTwo + 2
    return output
sum = addOneAddTwo(var2,var)

print(sum)


