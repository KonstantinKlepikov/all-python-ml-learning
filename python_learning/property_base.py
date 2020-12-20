# basic example of property

class Person:

    
    def __init__(self, name):
        self.name_ = name

    def getName(self):
        print('fetch...')
        return self.name_

    def setName(self, value):
        print('change...')
        self.name_ = value

    def delName(self):
        print('remove...')
        del self.name_
    
    name = property(getName, setName, delName, 'name property doc')


# calculated attributes
class PropSquare:


    def __init__(self, start):
        self.value = start

    def getX(self):
        return self.value ** 2

    def setX(self, value):
        self.value = value

    X = property(getX, setX)


# decorators for propertyes
class PersonDec:

    def __init__(self, name):
        self._name = name

    @property # getter name is added automaticaly as first argument of property
    def name(self):
        """Name property docs string
        """
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


if __name__ == "__main__":
    
    def tester(class_):
        print('='*30)
        bob = class_('Bob Smith')
        print(bob.name)
        bob.name = 'Robert Smith'
        print(bob.name)
        del bob.name
        print('-'*30)
        sue = class_('Sue Jons')
        print(sue.name)
        print(class_.name.__doc__)
        print('='*30)

    tester(Person)


    P = PropSquare(3)
    Q = PropSquare(32)
    print(P.X)
    P.X = 4
    print(P.X, Q.X)


    tester(PersonDec)