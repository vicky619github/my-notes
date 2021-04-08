# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:04:46 2021

@author: vignesh jaishankar
"""


word = "hello"

letters = []

for w in word :
    print(w)
    if w =="e":
        print("what a funnny letter")
        
    letters.append(w)
print(letters)

for l in letters:
    print(l)
    


   
numbers = [1, 2, 3, 4, 5]
for l in numbers :
    if l%2 == 1:
        print(l)
        
        

for num in range(10):
    print(num)
    

numbers = []
for num in range(1,10,2):
    numbers.append(num)
    print(num)
print(numbers)
