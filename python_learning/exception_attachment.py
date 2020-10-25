# example of attachment of exception construction

def action2():
    print(1 + []) # here we generate TypeError

def action1():
    try:
        action2()
    except TypeError: # this is last operathor in a stack - it works
        print('inner try')

try:
    action1()
except TypeError: # this works only if we caugch secondary TypeError
    print('outer try')

# attachment (lasd used)
try:
    try:
        action2()
    except TypeError: # we a here
        print('Inner try with attachmetn')
except TypeError: # here only in secondary case
    print('outher try with exception')
    
# attachment and finaly (all used)
try:
    try:
        raise IndexError
    except IndexError:
        print('exception')
    finally:
        print('spam')
finally:
    print('SPAM')
"""
exception
spam
SPAM
"""