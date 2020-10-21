# example of try/finally

class MyError(Exception):
    pass


def stuff(file):
    raise MyError()

file = open('data', 'w')

try:
    stuff(file)
finally:
    file.close()
    print('is closed')
print('We are here only if no exception')

"""
is closed
Traceback (most recent call last):
File "finally.py", line 13, in <module>
stuff(file)
File "finally.py", line 8, in stuff
raise MyError()
__main__.MyError
"""
