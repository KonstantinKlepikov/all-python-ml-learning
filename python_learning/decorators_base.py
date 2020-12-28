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


if __name__ == "__main__":

    spam(1, 2, 3)
    spam('a', 'b', 'c')
    spam.calls
    print(spam)


    # attributes of class instances
    spam1(1, 2, 3)
    spam1(a=4, b=5, c=6)
    eggs(2, 16)
    eggs(2, y=4)