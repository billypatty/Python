"""
question:

Given a string, return a new string where the first and last chars have been exchanged.

my solution:
"""

def front_back(s):
    if len(s) <= 1: # if the string is empty or a single letter only, there is nothing to flip
        return s
    else:
        copstr = '' # an empty string
        copstr += s[-1] # add to it the last letter
        for i in range(1, len(s) -1): #skip the first letter & go until the last letter 
            copstr += s[i] # generate the string using the loop
        copstr += s[0] # lastly, add the first letter to the string
        return copstr
