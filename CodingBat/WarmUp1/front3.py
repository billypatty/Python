"""
question:

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

my solution:
"""

def front3(s):
  if len(s) <=3:
    return str*3 
  else:
    a = ''
    for i in range(3): 
        a += s[i] 
    return a*3 
