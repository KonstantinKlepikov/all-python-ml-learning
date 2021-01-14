# example of attr value check before assignment by decorator

def rangetest(*argchecks): # check for position args

    def onDecorator(func):
        if not __debug__: # True if python -O this.py
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        raise TypeError('Arg {0} not in {1}...{2}'.format(ix, low, high))
                return func(*args)
            return onCall
    return onDecorator

print(__debug__)

@rangetest((1, 0, 120))
def persinfo(name, age):
    print('{} is {} years old'.format(name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {}/{}/{}'.format(M, D, Y))

class Person:

    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])
    def giveRise(self, percent): # arg 0 hier is an instance self
        self.pay = int(self.pay * (1 + percent))


if __name__ == "__main__":

    persinfo('Bob Smith', 45)

    # use python -O, or is excepted
    try:
        persinfo('Bob Smith', 200)
    except TypeError as e:
        print(e)

    birthday(5, 31, 1963)

    # use python -O, or is excepted
    try:
        birthday(5, 32, 1963)
    except TypeError as e:
        print(e)

    sue = Person('Sue', 'dev', 10000)
    sue.giveRise(.10)
    print(sue.pay)

    # use python -O, or is excepted
    try:
        sue.giveRise(1.10)
    except TypeError as e:
        print(e)
