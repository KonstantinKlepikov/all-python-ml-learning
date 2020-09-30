# example of diamond-chime with MRO in python 3.x

class A:

    attr = 1
    def method(self):
        print('A.method')


class B(A):

    def method(self):
        print('B.method')


class C(A):

    attr = 2


class C1:

    pass


class D(B, C): # check C befor A

    attr1 = B.attr # choice route - A before B
    method = C.method # choice method A before B

    """
    # more explicid solution
    def method(self): # redefine

        C.method(self) # call for C -> A
    """

class D1(B, C1): # inheritans without diamond

    pass


if __name__ == "__main__":

    x = D() # search in x, D, B, C, A
    print(x.attr) # 2
    print(x.attr1) # 1
    x.method() # A.method

    # MRO
    print(D.__mro__) # D, B, C, A, object

    # non-diamond cheeme
    print(D1.__mro__) # D1, B, A, C1, object