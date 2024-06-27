"""
question:

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

my solution:
"""

def sleep_in(w, v): # w for weekday and v for vacation
    if not w: # if it is not a weekday,
        return True # regardless of the value of v, we will sleep in.
    elif w: # if it is a weekday,
        return v # if we are on a vacation, we'll sleep in. otherwise, we won't.
