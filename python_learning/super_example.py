# example of super() usage

"""Traditional method of superclass calling
"""

class C:

    def act(self):
        print('spam')


class D(C):

    def act(self):
        C.act(self) # explicit usage of superclass name to give it to self
        print('eggs')


class DSuper(C):

    def act(self):
        super().act() # link to superclass without self
        print('eggs')


class A:

    def act(self):
        print('not spam')


class Trap1(C, A): # mixed class

    def act(self):
        super().act() # choice only C method!

class Trap2(A, C): # mixed class

    def act(self):
        super().act() # choice only A method!

class E(C, A): # transitive form

    def act(self):
        print('transitive:')
        A.act(self)
        C.act(self)


if __name__ == "__main__":

    X = D()
    X.act() # spam eggs

    Y = DSuper()
    Y.act() # spam eggs

    Z1 = Trap1()
    Z1.act() # spam

    Z2 = Trap2()
    Z2.act() # not spam

    trans = E()
    trans.act() # spam not spam