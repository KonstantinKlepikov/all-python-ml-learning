# indexing with __getitem__ и __setitem__

class SimpleIndexer:

    def __getitem__(self, index):
        """Return *2 value with index operathor

        Args:
            index (int): position of index

        Returns:
            int: indexed value
        """
        return index ** 2

class IndexAndSlice(SimpleIndexer):

    def __getitem__(self, index):
        """Print *2 value if index, or slice attrs if slice

        Args:
            index (int): position of index 
            or slice attributes start:ens:step
        """
        if isinstance(index, int):
            print('indexing - index * 2 =', index * 2)
        else:
            print('slicing', index.start, index.stop, index.step)

class StepperIndex(SimpleIndexer):

    def __getitem__(self, i):
        """Example of realisation for operathor:
        if __getitem__() is define, we can us it for operathor 'for',
        because 'for; is a step by step index, for as long IndexError
        isnt rised

        Args:
            SimpleIndexer (object): iterated object

        Returns:
            obj: if indexing - indexed element * 2, if indexing in 'for' - 
            result of operations inside 'for' * 2
        """
        return self.data[i] * 2


if __name__ == '__main__':

    X = SimpleIndexer()
    for i in range(5):
        print(X[i], end=' ')
    Y = IndexAndSlice()
    Y[7]
    Y[1:22:2]
    Y[1:]

    Z = StepperIndex()
    Z.data = 'Spam'
    print(Z[-1]) # __getitem__ for indexing
    for item in Z: # __getitem__ for 'for' cycle
        print(item, end=' ') 

