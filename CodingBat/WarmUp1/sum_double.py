"""
question:

Given two int values, return their sum. Unless the two values are the same, then return double their sum.

my solution:
"""

def sum_double(a, b): # a function that sums the values according to the prompt.
    if a==b: # if the number a and b are equal,
        return 2*(a+b) # sum them, then multiply by two
    else:
        return a+b # sum them
