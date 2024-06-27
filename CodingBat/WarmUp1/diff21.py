"""
question:

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

my solution:
"""

def diff21(a): # define a function with a single input, an integer.
    if a<=21: # if that integer is not greater than 21,
        return abs(a-21) # use the 'abs' function to return their absolute value
    else: # other cases 
        return 2*abs(a-21) # multiply the absolute value by two.
