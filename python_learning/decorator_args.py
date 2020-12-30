# example of decorators arguments

def tracker(label=''):
    def decorator(func):
        def onCall(*args):
            func(*args)
            print(label)
        return onCall
    return decorator

@tracker('^^^')
def tester(a):
    print(a)


import time, sys

force = list if sys.version_info[0] == 3 else [lambda X: X]

def timer(label='', trace='True'):

    class Timer:

        def __init__(self, func):
            self.alltime = 0
            self.func = func

        def __call__(self, *args, **kwargs):
            start = time.process_time()
            result = self.func(*args, **kwargs)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            if trace:
                print('{0} {1}: {2}, {3}'.format(label, self.func.__name__, elapsed, self.alltime))
            return result

    return Timer


@timer('==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


if __name__ == "__main__":

    tester('this')

    result = listcomp(5)
    listcomp(50000)
    listcomp(500000)
    listcomp(1000000)
    print(result)
    print('allTime = {}'.format(listcomp.alltime))
    print('-' * 50)