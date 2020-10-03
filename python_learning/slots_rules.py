# example of __slots__ rules

#slots in subclass, but not in superclass
class C:

    pass


class D(C):

    __slots__ = ['a']


# __slots__ in superclass, but not in subclass
class A:

    __slots__ = ['a']


class B(A):

    pass


# available only last __slots__
class Z:

    __slots__ = ['a']

class E(Z):

    __slots__ = ['b']


# standard names of class level is unavailable
class F:
    __slots__ = ['a']
    # a = 99 # ValueError: 'a' in __slots__ conflicts with class variable


if __name__ == "__main__":

    X = D() # __dict__is created
    X.a = 1
    X.b = 2
    print(X.__dict__) # {'b': 2}
    print(D.__dict__.keys()) # dict_keys(['__module__', '__slots__', 'a', '__doc__'])


    Y = B()
    Y.a = 1
    Y.b = 2
    print(Y.__dict__) # # {'b': 2}
    print(A.__dict__.keys()) # dict_keys(['__module__', '__slots__', 'a', '__doc__'])


    S = E()
    print(S.__slots__) # ['b']
