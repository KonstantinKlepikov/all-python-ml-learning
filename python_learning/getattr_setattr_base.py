# base example of gettatr, setattr

# basic realisation
class Catcher:

    def __getattr__(self, name):
        print('Get: {0}'.format(name))

    def __setattr__(self, name, value):
        print('Set: {0}, {1}'.format(name, value))


# realisation with delegation
class Wrapper:

    def __init__(self, obj):
        self.wrapped = obj # save object

    def __getattr__(self, attrname):
        print('Trace:' + attrname) # trace the extraction
        return getattr(self.wrapped, attrname) # delegate extraction


# avoidance of recursive cicling

class Cycled:

    def __init__(self, other):
        self.other = other

    def __getattribute__(self, name): # extract all attributes
        x = self.other # infinite cycling!!!

# for solution use suoerclass for getattribute

# def __getattribute__(self, name):
#     x = obj.__getattribute__(self, 'other')

# !!! For method __setattr__ and __delattr__ all is analogic.
# For solution use definition as key in __dic__

# def __setattr__(self, name, value):
#   self.__dict__['other'] = value


# first most realistic example
class Person:

    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        print('get ' + attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print('set ' + attr)
        if attr == 'name':
            attr = '_name' # set inside name
        self.__dict__[attr] = value # prevent infinite cycling

    def __delattr__(self, attr):
        print('del ' + attr)
        if attr == 'name':
            attr = '_name' # set inside name
        del self.__dict__[attr] # prevent infinite cycling


# __gaetattribute__usage
class PersonGetattribute:

    def __init__(self, name):
        self._name = name # here is additional __setattr__ and we see it in instance usage

    def __getattribute__(self, attr):
        print('get ' + attr)
        if attr == 'name':
            attr = '_name' # set inside name
        return object.__getattribute__(self, attr)  # prevent infinite cycling

    def __setattr__(self, attr, value):
        print('set ' + attr)
        if attr == 'name':
            attr = '_name' # set inside name
        self.__dict__[attr] = value # prevent infinite cycling

    def __delattr__(self, attr):
        print('del ' + attr)
        if attr == 'name':
            attr = '_name' # set inside name
        del self.__dict__[attr] # prevent infinite cycling


# calculated attributes
class AttrSquare:

    def __init__(self, start):
        self.value = start

    def __getattr__(self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value


# calculated attributes with __getattribute__
class AttrSquareGetattribute:

    def __init__(self, start):
        self.value = start # here __setattr__ is started

    def __getattribute__(self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)


# comparison of __getattr__ and __getattribute__
class GetAttr:
    
    attr1 = 1
    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr): # intercept only undefibed attr3
        print('get ' + attr)
        if attr == 'attr3':
            return 3
        else:
            raise AttributeError(attr)

class GetAttribute:
    
    attr1 = 1
    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr): # intercept all attribute
        print('get ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


if __name__ == "__main__":

    X = Catcher()
    X.job # Get: job
    X.pay # Get: pay
    X.pay = 99 # Set: pay, 99
    print(X.pay) # None

    Y = Wrapper([1, 2, 3])
    Y.append(4) # Trace:append
    print(Y.wrapped) # [1, 2, 3, 4]


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
        try: 
            print(class_.name.__doc__) # attr is only inside of methods
        except AttributeError as a:
            print(a)
        print('='*30)

    tester(Person)
    tester(PersonGetattribute)

    P = AttrSquare(3)
    Q = AttrSquare(32)
    print(P.X)
    P.X = 4
    print(P.X, Q.X)
    print('='*30)

    P = AttrSquareGetattribute(3)
    Q = AttrSquareGetattribute(32)
    print(P.X)
    P.X = 4
    print(P.X, Q.X)
    print('='*30)


    X = GetAttr()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)
    print('='*30)

    X = GetAttribute()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)
    print('='*30)
