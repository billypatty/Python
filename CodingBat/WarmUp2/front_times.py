"""
question:

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Return n copies of the front.

my solution:
"""

def front_times(s, n):
  if len(s) <= 3: # check if the word is shorter than 3 letters
    return s*int(n)
  else: # if it isn't,
    a = ''
    for i in range(3):
      a += s[i]
    return a*int(n)
