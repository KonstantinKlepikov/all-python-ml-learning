# basic examples of decorators realisation

# call tracking
class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)


# preserving states for decorators

# attributes of class instances
class tracerAttr:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@tracerAttr
def spam1(a, b, c):
    print(a + b + c)

@tracerAttr
def eggs(x, y):
    print(x ** y)


# state from enclosing area of vision and global variable

calls = 0 # is global and is changed by each call

def tracerEnc(func):

    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print('call {0} to {1}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper

@tracerEnc
def spam2(a, b, c):
    print(a + b + c)

@tracerEnc
def eggs1(x, y):
    print(x ** y)


# state from enclosing area of vision and nonlocal variable

def tracerEncNonloc(func):

    calls = 0 # is nonlocal and work as class attribute

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {0} to {1}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper

@tracerEncNonloc
def spam3(a, b, c):
    print(a + b + c)

@tracerEncNonloc
def eggs2(x, y):
    print(x ** y)


# function attributes
def tracerAttrFunc(func):

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('call {0} to {1}'.format(wrapper.calls, func.__name__))
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@tracerAttrFunc
def spam4(a, b, c):
    print(a + b + c)

@tracerAttrFunc
def eggs3(x, y):
    print(x ** y)

if __name__ == "__main__":

    spam(1, 2, 3)
    spam('a', 'b', 'c')
    spam.calls
    print(spam)
    print('=' * 50)


    # attributes of class instances
    spam1(1, 2, 3)
    spam1(a=4, b=5, c=6)
    eggs(2, 16)
    eggs(2, y=4)
    print('=' * 50)

    # enclousing area global
    spam2(1, 2, 3)
    spam2(a=4, b=5, c=6)
    eggs1(2, 16)
    eggs1(2, y=4)
    print('=' * 50)

    # enclousing area nonlocal
    spam3(1, 2, 3)
    spam3(a=4, b=5, c=6)
    eggs2(2, 16)
    eggs2(2, y=4)
    print('=' * 50)

    # function attributes
    spam4(1, 2, 3)
    spam4(a=4, b=5, c=6)
    eggs3(2, 16)
    eggs3(2, y=4)
    print('=' * 50)

