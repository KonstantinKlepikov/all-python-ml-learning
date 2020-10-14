# example of advantages by using super()

"""Changing of classes in process
"""

class X:

    def m(self):
        print('X.m')


class Y:

    def m(self):
        print('Y.m')


class C(X):

    def m(self):
        super().m() # in that position we cant hardcode name of class


class D(X):

    def m(self):
        D.__bases__[0].m(self) # alternative without super()


"""Usage of super() for class constructors
"""

class B:

    def __init__(self):
        print('B.__init__')


class E:

    def __init__(self):
        print('E.__init__')


class J(B, E):
    pass


class Jname(B, E):

    def __init__(self): # calling by name (trditional cheeme)
         B.__init__(self)
         E.__init__(self)

# super cheme (MRO usage)
class Sup1(B):

    def __init__(self):
        print('Sup1.__init__')
        super().__init__()

class Sup2(B):

    def __init__(self):
        print('Sup2.__init__')
        super().__init__()

# rondo
class SupSup(Sup1, Sup2):
    pass


if __name__ == "__main__":
    
    i = C()
    i.m()

    C.__bases__= (Y,) # we change superclass in process
    i.m()

    i = D()
    i.m()
    D.__bases__= (Y,)
    i.m()

    x = J() # B.__init__
    x = Jname() # B.__init__ E.__init__

    print('super cheme')
    x = Sup1() # Sup1.__init__ B.__init__
    x = Sup2() # Sup2.__init__ B.__init__
    x = SupSup() # Sup1.__init__ Sup2.__init__ B.__init__
