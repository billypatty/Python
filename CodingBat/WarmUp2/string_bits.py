"""
question:

Given a string, return a new string made of every other char starting with the first,
so "Hello" yields "Hlo".

my solution:
we should be careful about words with even number of letters.
"""

def string_bits(s):
  a = '' # define an empty string
  for i in range(len(s)): # for every letter in 's' times,
    if i%2==0: # (remember that indexing starts at 0)
      a += s[i] # add it to the initially empty string
  return a
