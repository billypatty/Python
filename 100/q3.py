# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:48:03 2024.

q: With a given integral number n, write a program to generate a dictionary 
that contains (i, i*i) such that is an integral number between 1 and 
n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

@author: billypatty
"""

# assuming n is always an integer and nothing else

n = int(input("give an integer: "))
someDict = {}
for i in range(n):
    someDict[i+1] = (i+1)**2
print(someDict)
