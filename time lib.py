# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:05:49 2021

@author: vignesh jaishankar
"""

import time
currentTime = time.clock()
print("Hello")
print("world")
pastTime = time.clock()
print(pastTime - currentTime)

print("1")
time.sleep(3)
print("2")

for i in range(1,11):
    print(i)
    time.sleep(1 )