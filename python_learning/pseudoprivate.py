# example of pseudoprivate solution for class attributes, metods and etc

class NonPrivate1:

    def meth1(self):
        self.X = 100 # X is my

    def meth2(self):
        print(self.X)


class NonPrivate2:

    def metha(self):
        self.X = 200 # i think X is my

    def methb(self):
        print(self.X)


class NonPrivate3(NonPrivate1, NonPrivate2):
    pass

# pseudoprivate
class Private1:

    def meth1(self):
        self.__X = 100 # X is my

    def meth2(self):
        print(self.__X)


class Private2:

    def metha(self):
        self.__X = 200 # i think X is my

    def methb(self):
        print(self.__X)


class Private3(Private1, Private2):
    pass


# example
class Main:
    def method(self): # main method
        print('Main')


class Tool:
    def __method(self): # _Tool__method
        print('Tool')

    def other(self): # usage of inside method
        self.__method()


class Sub1(Tool, Main):
    def actions(self):
        self.method() # usage of Main.method
        self.other()
        self._Tool__method() # deprivatisation
    

class Sub2(Tool):
    def __init__(self):
        self.method = 99 #new method, that cant overrite _Tool__.method


if __name__ == "__main__":

    # only one X - last in tree of inheritance
    I = NonPrivate3()
    I.meth1()
    I.metha()
    print(I.__dict__)
    I.meth2()
    I.methb()

    # now in I two X
    I = Private3()
    I.meth1()
    I.metha()
    print(I.__dict__)
    I.meth2()
    I.methb()

    x = Sub1()
    x.actions()

    z = Sub2()
    print(z.method)