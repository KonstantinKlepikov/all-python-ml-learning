# example of usage exception for case, where needed for signals

class Found(Exception):
    pass


class Failure(Exception):
    pass


def searcher1(x, y):
    for i in list(range(x)):
        if i == y:
            raise Found()

try:
    searcher1(10, 5)
except Found:
    print('success')
else:
    print('unsuccess')
# success


def searcher2(x, y):
    for i in list(range(x)):
        if i == y:
            return i
    raise Failure()

try:
    result = searcher2(10, 5)
except Failure:
    print('unsuccess')
else:
    print(result)
# 5
