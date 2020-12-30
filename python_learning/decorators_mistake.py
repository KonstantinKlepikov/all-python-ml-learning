# example of decorators mistake

# exemplar of decorated class cant put into *args
class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


class Person:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer 
    def lastName(self):
        return self.name.split()[-1]


# solution - inside function (in example with nonlocal variable)
def tracerEncNonloc(func):

    calls = 0 # is nonlocal and work as class attribute

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {0} to {1}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


class Person1:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracerEncNonloc
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracerEncNonloc
    def lastName(self):
        return self.name.split()[-1]


# descriptors solution
class tracerDesc:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapperDesc(self, instance)

class wrapperDesc:

    def __init__(self, desc, subj): # savw both instances
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs) # tracerDesc.__call__ start


class Person2:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracerDesc
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracerDesc
    def lastName(self):
        return self.name.split()[-1]


# alternative
class tracerDescNoWrap:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


class Person3:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracerDescNoWrap
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracerDescNoWrap
    def lastName(self):
        return self.name.split()[-1]



    
if __name__ == "__main__":
    
    bob = Person('Bob Smith', 50000)
    try:
        bob.giveRaise(.25) # giveRaise() missing 1 required positional argument: 'percent'
    except TypeError as a:
        print(a)

    try:
        print(bob.lastName()) # lastName() missing 1 required positional argument: 'self'
    except TypeError as a:
        print(a)
    print('-' * 50)

    
    bob = Person1('Bob Smith', 50000)
    bob.giveRaise(.25)
    print(bob.pay)
    print(bob.lastName())
    print(bob.lastName())
    print('-' * 50)


    bob = Person2('Bob Smith', 50000)
    bob.giveRaise(.25)
    print(bob.pay)
    print(bob.lastName())
    print(bob.lastName())


    bob = Person3('Bob Smith', 50000)
    bob.giveRaise(.25)
    print(bob.pay)
    print(bob.lastName())
    print(bob.lastName())
