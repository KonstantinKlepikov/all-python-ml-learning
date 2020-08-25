class MixedNames:
    """Example of attributes
    """

    data = 'spam' #class attribure

    def __init__(self, value):
        self.data = value # exemplar attribute

    def display(self):
        # show class attr and exemplar attr
        print(self.data, MixedNames.data)


class NextClass:

    def printer(self, text):
        self.message = text
        print(self.message)


class Parrent:
    def __init__(self, x):
        pass


class Child(Parrent):
    def __init__(self, x, y):
        Parrent.__init__(self, x) #run __init__ of superclass
        pass

# example of replacement method
class Parrent1_rep:

    def method(self):
        print('It is Parrent_rep.method')


class Child_rep(Parrent1_rep):

    def method(self): # replace method
        print('starting Child_rep.method')
        Parrent1_rep.method(self) # call for original method
        print('endingChild_rep.method')


if __name__ == "__main__":

    x = MixedNames(1)
    y = MixedNames(2)
    # exemplar sttr different in different exemplar
    # class attr same, is in class and in exemplar
    x.display(), y.display()

    # That forms of wrighting are equivalent
    x.display()
    MixedNames.display(x)

    z = NextClass()
    # call to method from exemplar
    z.printer('some text')
    print(z.message)
    # direct call from class
    NextClass.printer(z, 'class call')
    print(z.message)

    # __init__ inheritans
    I = Child(1, 2)

    # example of replacement method
    xr = Parrent1_rep()
    xr.method()

    xr = Child_rep()
    xr.method()
