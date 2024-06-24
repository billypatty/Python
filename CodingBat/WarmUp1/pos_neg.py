"""
question:

Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.

my solution:
"""

def pos_neg(a, b, negative):
  if negative == False:
    if a < 0 and b < 0: # if both numbers are negative,
      return False
    elif a<0 or b<0: # if either is negative,
      return True
    else:  # if none of them is negative,
      return False
  elif negative == True:
    if a <0 and b<0: # making sure both numbers are negative
      return True
    else:
      return False
  
