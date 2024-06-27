"""
question:

Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.

my solution:
'within 10 of' means we're looking for a number either 90-110 or 190-210.
"""

def near_hundred(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10: # by using 'abs', we make sure the value is correct
        return True # for example, if n is 230, 200-230=-30 which is less than 10.
    else: # other cases
        return False
