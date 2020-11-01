# example of overloading __lt__, __gt__ 

class C:
    """Overloading __lt__ and __gt__
    """

    data = 'spam'
    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


if __name__ == "__main__":
    X = C()
    print(X > 'ham') # True __gt__
    print(X < 'ham') # false __lt__