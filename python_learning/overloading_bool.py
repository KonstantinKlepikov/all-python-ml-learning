# overloading __bool__

class Truth:

    def __bool__(self):
        return True

class Lie:

    def __bool__(self):
        return False

class TruthNoBool:
    """Example with __len__
    """
    def __len__(self):
        return 0

class TruthBoolPriority:
    """If booth __bool__ and __len__ - 
    __booll__ is in ptiority in python3.x
    """
    def __bool__(self):
        return True
    def __len__(self):
        return 0

class NoOne:
    pass

if __name__ == "__main__":
    X = Truth()
    if X:
        print('Yes!')

    print(bool(X))

    Y = Lie()
    if not Y:
        print('Not!')

    print(bool(Y))

    Z = TruthNoBool()
    if not Z:
        print('Not!')

    W = TruthBoolPriority()
    if W:
        print('Not!')

    Q= NoOne()
    print(bool(Q)) # if no one defined - is True
