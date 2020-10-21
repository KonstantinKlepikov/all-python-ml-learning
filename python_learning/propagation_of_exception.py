# example of raise usage

try:
    raise IndexError('spam') # storage arguments
except IndexError:
    print('propagating')
    raise # reusage of exception

"""
propagating
Traceback (most recent call last):
File "propagation_of_exception.py", line 4, in <module>
raise IndexError('spam') # storage arguments
IndexError: spam
"""