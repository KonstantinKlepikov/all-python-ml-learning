# simple example of operathors overloading

class Number:

    def __init__(self, start):
        """Define attr for Number

        Args:
            start (int): any number
        """
        self.data = start
    
    def __sub__(self, other):
        """Overload sub operation for exemplars of Number

        Args:
            other (int): any number

        Returns:
            obj: new exemplar is returned
        """
        return Number(self.data - other)


if __name__ == '__main__':

    X = Number(5) # Number.__init__(X, 5)
    print(X)
    Y = X - 2 # Number.__sub__(X, 2)
    print(Y)
    Z = Y.data # is new exemplar of Number
    print(Z)