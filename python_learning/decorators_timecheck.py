# example of timecheck, realised as decorator

import time, sys

force = list if sys.version_info[0] == 3 else [lambda X: X]

class timer:

    def __init__(self, func):
        self.alltime = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.process_time()
        result = self.func(*args, **kwargs)
        elapsed = time.process_time() - start
        self.alltime += elapsed
        print('{0}: {1}, {2}'.format(self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = {}'.format(listcomp.alltime))
print('-' * 50)

result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = {}'.format(mapcall.alltime))
print('-' * 50)
