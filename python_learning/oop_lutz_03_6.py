# example of nonlinear + realisation

class Computation1:

    def __init__(self, value):
        self.value = value

    def __add__(self, other): # for obj + exemplar
        print('add', self.value, other, sep=' ')
        return self.value + other

    def __radd__(self, other): # for exemplar + obj
        print('add', other, self.value, sep=' ')
        return other + self.value # !inversed order


# other realisations
class Computation2:
    """Reusage of __add__
    """
    def __init__(self, value):
        self.value = value

    def __add__(self, other): 
        print('add', self.value, other, sep=' ')
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)


class Computation3:
    """Change position and sum again
    """
    def __init__(self, value):
        self.value = value

    def __add__(self, other): 
        print('add', self.value, other, sep=' ')
        return self.value + other

    def __radd__(self, other):
        return self + other


class Computation4:
    """Use pseudonime
    """
    def __init__(self, value):
        self.value = value

    def __add__(self, other): 
        print('add', self.value, other, sep=' ')
        return self.value + other

    __radd__ = __add__


class Computation5:

    """UProliferation of class type
    """
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Computation5): #check type to prevent nesting
            other = other.value
        return Computation5(self.value + other)

    def __radd__(self, other):
        return Computation5(other + self.value)

    def __str__(self):
        return '<Computation5>: {0}'.format(self.value)


if __name__ == "__main__":

    for class_ in (
        Computation1,
        Computation2,
        Computation3,
        Computation4,
        Computation5
        ):
        print('-'*60) 
        x = class_(22)
        y = class_(66)
        print(x + 1)
        print(1 + y)
        print(x + y) # __add__ is wrongr

        z = x + y
        print(z + z + 1)
