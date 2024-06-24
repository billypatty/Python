"""
question:

Given a string, return a new string where the first and last chars have been exchanged.

my solution:
"""

def front_back(str):
  if len(str) <= 1: # if the string is empty or a single letter only, there is nothing to flip
    return str
  else:
    copstr = '' # an empty string
    copstr += str[-1] # add to it the last letter
    for i in range(1, len(str) -1): #skip the first letter & go until the last letter 
      copstr += str[i] # generate the string using the loop
    copstr += str[0] # lastly, add the first letter to the string
    return copstr
