"""
question:

Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

my solution:
"""

def missing_char(s, n): # s for the string input, n for the index
    a = '' # an empty string
    b=[] # an empty list
    for i in s: # for every letter in the given input,
        b.append(i) # add it to the list.
    c=b[n] # c is equal to what we want to remove
    b.remove(c) # remove that from the list
    for j in b: # for every letter in the list,
        a += str(j) # convert it to string and add it to the initially empty string 'a'
    return a
