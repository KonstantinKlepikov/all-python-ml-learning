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


if __name__ == '__main__':

    X = SimpleIndexer()
    for i in range(5):
        print(X[i], end=' ')
    Y = IndexAndSlice()
    Y[7]
    Y[1:22:2]
    Y[1:]

