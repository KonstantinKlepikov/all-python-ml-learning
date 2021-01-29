# example of colaborative usage of metaclasses and/or decorators

# trace with decorators
import time

def tracer(func): # we use function, but no __call__ method of class
    
    calls = 0

    def onCall(*args, **kwargs):

        nonlocal calls
        calls += 1
        print('call {} to {}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return onCall

def timer(label='', trace=True): # if decoreator has args - save args

    def onDecorator(func): # with @ save decoratedfunction

        def onCall(*args, **kwargs): # with calls - call initial function

            start = time.clock()

            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed

            if trace:
                format_ = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format_ % values)

            return result
        
        onCall.alltime = 0

        return onCall

    return onDecorator


class Person:

    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


    @tracer
    def lastName(self):
        return self.name.split()[-1]


# tracing with metaclasses and decorators
from types import FunctionType


class MetaTrace(type):

    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType: # if it is method
                classdict[attr] = tracer(attrval)
        return type.__new__(meta, classname, supers, classdict) # create a class


class Person1(metaclass=MetaTrace):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


# the fabric of metaclasses - decorate with any decorator
def decorateAll(decorator):

    class MetaDecorate(type):

        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)

    return MetaDecorate


class Person2(metaclass=decorateAll(tracer)):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


class Person3(metaclass=decorateAll(timer())):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


class Person4(metaclass=decorateAll(timer(label='**'))):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


# decorator of classes as alternative of metaclass
def decorateAlldec(decorator):

    def DecoDecorate(aClass):

            for attr, attrval in aClass.__dict__.items():
                if type(attrval) is FunctionType:
                   setattr(aClass, attr, decorator(attrval))
            return aClass

    return DecoDecorate


@decorateAlldec(tracer)
class Person5:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


@decorateAlldec(timer())
class Person6:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


@decorateAlldec(timer(label='++++'))
class Person7:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]
    

if __name__ == "__main__":
    
    def functest(class_):
        bob = class_('Bob Smith', 50000)
        sue = class_('Sue Jones', 100000)
        print(bob.name, sue.name)
        sue.giveRaise(.25)
        print(bob.pay)
        print('{}'.format(sue.pay))
        print(bob.lastName(), sue.lastName())
        print('-'*50)

    functest(Person)
    functest(Person1)
    functest(Person2)
    functest(Person3)
    functest(Person4)
    functest(Person5)
    functest(Person6)
    functest(Person7)
