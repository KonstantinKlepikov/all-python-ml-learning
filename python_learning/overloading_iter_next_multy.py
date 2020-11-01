# example of overloading __iter__ and __next__ - multy iteration

class SkipObject:
    """Return nefw iterator every time for each __iter__() call
    """
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    """Multiply iteration
    """

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0 # iterators counter

    def __next__(self):
        if self.offset >= len(self.wrapped): # stop iteration
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # iteration
            self.offset += 2
            return item

if __name__ == '__main__':

    text = 'abcde'
    skipper = SkipObject(text)
    I = iter(skipper) # indexes
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print((x + y)*2, end=' ')
