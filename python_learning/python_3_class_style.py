class C:
    pass

class D:
    pass

if __name__ == "__main__":

    X = C()

    print(type(X)) # type of exemplar is a class
    print(X.__class__)

    print(type(C)) # class is a type, type is a class
    print(type(C.__class__))

    print(type([1, 2, 3])) # classes and embedded types works same
    print([1, 2, 3].__class__)
    print(type(list))
    print(list.__class__)

    # comparison

    c, d = C(), D()
    # comparison by classes of exemplars
    print(type(c) == type(d)) # False
    c1, c2 = C(), C()
    print(type(c1) == type(c2)) # True


    X.normal = lambda: 99
    print(X.normal()) # normal methods still come from exemplars

    X.__add__ = lambda y: 88 + y # same for embedded names
    X.__add__(1)

    X + 1 # but not for sentencies
    # TypeError: unsupported operand type(s) for +: 'C' and 'int'
