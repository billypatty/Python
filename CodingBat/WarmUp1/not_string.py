"""
question:

Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged. 

my solution:
"""

def not_string(str):
    k = str.split(' ') # divide the given string from its spaces
    if k[0] == 'not': # if the first element is 'not'
        return str
    else:
        return 'not ' + str # return 'not' and the string after it, making the first word 'not'.
