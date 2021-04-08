# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:40:30 2021

@author: vignesh jaishankar
"""
#from random import *
import random as pee 

pee.seed(2)
randInt = pee.randint(0,10)
print(randInt)

randomFloat = pee.random()
print(randomFloat)

randomUniform = pee.uniform(1,1100)
print(randomUniform)


simpleList = [1,3,5,7,11]
pickElement = pee.choice(simpleList)
print(pickElement)
print(simpleList)
pee.shuffle(simpleList)
print(simpleList)