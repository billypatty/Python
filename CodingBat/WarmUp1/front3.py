"""
question:

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

my solution:
"""

def front3(s):
  if len(s) <=3: # if the string is shorter than 3 letters,
    return str*3 # return whatever
  else: # is its longer,
    a = '' # an empty string
    for i in range(3): # the loop will repeat 3 times
      a += s[i] # add the letter at index i to the initially empty string 'a'
    return a*3 # repeat a three times
