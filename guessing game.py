# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:19:35 2021

@author: vignesh jaishankar
"""

from random import randint
randVal = randint(0,100)

while(True):
    guess = int(input("pls enter your guess : "))
    if guess == randVal :
        break
    elif guess < randVal:
        print("your guess is too low")
    else :
        print("too high")

print("you have guessed corrctly with : ",guess)
    