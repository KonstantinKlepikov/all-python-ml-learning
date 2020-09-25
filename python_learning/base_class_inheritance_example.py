# example of extending by class creation as base class child


class MyList(list):

    """Displays 1...N to 0... N-1
    """

    def __getitem__(self, offset):
        print('(indexing {0} at {1})'.format(self, offset))
        return list.__getitem__(self, offset - 1)


if __name__ == "__main__":

    print(list('abc'))

    x = MyList('abc') # __init__, inherited from list
    print(x) # __repr__, inherited from list

    print(x[1]) # MyList.__getitem__ tune method from list
    print(x[3])

    x.append('spam') # attrs from list
    print(x)

    x.reverse()
    print(x)

