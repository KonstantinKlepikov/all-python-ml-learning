# example of custom decorator

# function decorator
class Tracer:

    def __init__(self, func): # storage base scoring

        self.calls = 0
        self.func = func

    def __call__(self, *args):

        self.calls += 1
        print('Call {0} to {1}'.format(self.calls, self.func.__name__))
        return self.func(*args)

@Tracer
def spam(a, b, c):
    return a + b + c


if __name__ == "__main__":

    # call for @Tracer first
    print(spam(1, 2, 3)) # call 1 to spam 6
    print(spam('a', 'b', 'c')) # call 2 to spam abc
