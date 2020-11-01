# example of 3 methods for iterations and checking of containing

class Iters:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        """Variant for iterations, etc. indexing anf slicing

        Args:
            i (int): nimber for indexing

        Returns:
            obj: 
        """
        print('get[{}]:'.format(i), end='')
        return self.data[i]

    def __iter__(self):
        """For iteration. Can be only one active iterathor

        Returns:
            obj: iterathor
        """
        print('iter=> ', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        """For in operation

        Args:
            x (obj): 

        Returns:
            bool: 
        """
        print('contains: ', end=' ')
        return x in self.data

class ItersYield(Iters):
    """Yield variant
    """

    def __init__(self, value):
        Iters.__init__(self, value)

    def __iter__(self):
        """For iteration with multiple iterathors
        """
        print('iter=> next:', end=' ')
        for x in self.data:
            yield x
            print('next:', end=' ')


if __name__ == '__main__':

    def test_func(exemplar):
        print(3 in exemplar) # in
        for i in exemplar: # cycle for
            print(i, end=' | ')
        print([i ** 2 for i in exemplar]) # example of other contexts

        I = iter(exemplar) # hand iteration

        while True:
            try:
                print(next(I), end=' @ ')
            except StopIteration:
                break

    test_func(Iters([1, 2, 3, 4, 5]))

    test_func(ItersYield([1, 2, 3, 4, 5]))

"""If exclude __contains__method - contain operations 
is used by __iter__ method. If we exclude __iter__ - by
__getitem__ method
"""



