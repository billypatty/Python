"""
question:

Given a non-empty string like "Code" return a string like "CCoCodCode".

my solution:
"""

def string_splosion(s):
  a = '' # an empty string
  for i in range(len(s)): # repeat it for every leter in the word 's',
    for j in range(0,i): # from the first letter, go until the ith letter,
      a += s[j] # add it to the initially empty string 'a'
  a += s # also add the word itself, since range function doesn't cover all
  return a
