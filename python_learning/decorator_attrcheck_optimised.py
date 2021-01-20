# example of attr value check before assignment by decorator
# in this realisation check defauld values of attributes
# and key arguments

trace = True

def rangetest(**argchecks): # check for position and keys args, include args with defauld values

    def onDecorator(func):
        if not __debug__: # True if python -O this.py
            return func
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onCall(*pargs, **kargs):
                # in *pargs all elements is first N elements by position
                # **kargs - last or is skipped if defauld
                expected = list(allargs)
                positionals = expected[:len(pargs)]
                for (argname, (low, high)) in argchecks.items():
                    if argname in kargs:
                        if kargs[argname] < low or kargs[argname] > high:
                            msg = '{0} argument "{1}" not in {2}...{3}'.format(funcname, argname, low, high)
                            raise TypeError(msg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            msg = '{0} argument "{1}" not in {2}...{3}'.format(funcname, argname, low, high)
                            raise TypeError(msg)
                    else:
                        # for defauld value of args
                        if trace:
                            print('Argument "{0}" defaulded'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

print(__debug__)

@rangetest(age=(0, 120))
def persinfo(name, age):
    print('{} is {} years old'.format(name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {}/{}/{}'.format(M, D, Y))

class Person:

    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest(percent=(0.0, 1.0))
    def giveRise(self, percent): # arg 0 hier is an instance self
        self.pay = int(self.pay * (1 + percent))

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


if __name__ == "__main__":

    persinfo('Bob Smith', 45)
    persinfo(age=40, name='Sue Jones')

    # use python -O, or is excepted
    try:
        persinfo('Bob Smith', 200)
    except TypeError as e:
        print(e)

    # use python -O, or is excepted
    try:
        persinfo(age=150, name='Bob Smith')
    except TypeError as e:
        print(e)

    birthday(5, 31, 1963)
    birthday(5, D=20, Y=1975)

    # use python -O, or is excepted
    try:
        birthday(5, 32, 1963)
    except TypeError as e:
        print(e)

    # use python -O, or is excepted
    try:
        birthday(5, D=32, Y=1963)
    except TypeError as e:
        print(e)

    sue = Person('Sue', 'dev', 10000)
    sue.giveRise(.10)
    print(sue.pay)

    bob = Person('Bob', 'cock', 50000)
    bob.giveRise(percent=.20)
    print(sue.pay)

    # use python -O, or is excepted
    try:
        sue.giveRise(1.10)
    except TypeError as e:
        print(e)

    # use python -O, or is excepted
    try:
        bob.giveRise(percent=1.20)
    except TypeError as e:
        print(e)

    
    omitargs(1, 2, 3, 4)
    omitargs(1, 2, 3)
    omitargs(1, 2, 3, d=4)
    omitargs(1, d=4)
    omitargs(d=4, a=1)
    omitargs(1, b=2, d=4)
    omitargs(d=8, c=7, a=1)

    # use python -O, or is excepted
    try:
        omitargs(1, 2, 3, 11)
    except TypeError as e:
        print(e)
    try:
        omitargs(1, 2, 11)
    except TypeError as e:
        print(e)
    try:
        omitargs(1, 2, 3, d=11)
    except TypeError as e:
        print(e)
    try:
        omitargs(11, d=4)
    except TypeError as e:
        print(e)
    try:
        omitargs(d=4, a=11)
    except TypeError as e:
        print(e)
    try:
        omitargs(1, b=11, d=4)
    except TypeError as e:
        print(e)
    try:
        omitargs(d=8, c=7, a=11)
    except TypeError as e:
        print(e)
