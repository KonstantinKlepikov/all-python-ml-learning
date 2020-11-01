# example of overloading __iter__ and __next__

class Squares:

    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    
    def __iter__(self):
        """Return iterathor object
        """
        return self

    def __next__(self):
        """Return elements of iterathor

        Returns:
            obj: element of iterathor * 2
        """

        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

class SquiresYield(Squares):
    """Alternative realisation with yield
    __next__ is created automaticaly
    """

    def __init__(self, start, stop):
        Squares.__init__(self, start, stop)

    def __iter__(self):
        for value in range(self.value, self.stop):
            yield value ** 2

if __name__ == '__main__':

    X = Squares(1, 5)
    for i in X:
        print(i, end=' ')

    Y = SquiresYield(1, 5) # yield realisation
    for i in Y:
        print(i, end=' ')

    Z = SquiresYield(1, 5) # multyply iteration inbox for yield realisation
    for i in Z:
        for j in Z:
            print(j + i, end=' ')
