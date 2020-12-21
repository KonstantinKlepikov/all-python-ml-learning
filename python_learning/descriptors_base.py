# basic example of descriptors


class Descriptor:

    """Docstring

    instance - is a exemplar of descriptor

    owner - class, that attached by descriptor
    """
    def __get__(self, instance, owner):
        # return value of attribute
        pass

    def __set__(self, instance, value):
        # nothing to return (None)
        pass

    def __delete__(self, instance):
        # nothing to return (None)
        pass


# most realistic example
class DescriptorReal:

    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:

    attr = DescriptorReal()


# descriptors attr only for reading
class D:

    def __get__(*args):
        print('get')

    def __set__(*args):
        # raise exception for readonly attribute
        raise AttributeError('cannot set - only for reading')


class C:

    a = D()


# example for  properties, rewrited by descriptors
class Name:

    """name descriptor docs
    """
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person:

    def __init__(self, name):
        self._name = name
    name = Name() # assign descriptor to attribute


# client inside version
class PersonIn:

    def __init__(self, name):
        self._name = name

    class Name:

        """name descriptor docs
        """
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()


# calculated attributes
class DescSquare:

    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        del self.value


class Client1:
    X = DescSquare(3)

class Client2:
    X = DescSquare(32)

# !!! Important: state of descriptor initialise data for each descriptors
# state of instance - data for each instance of client. You must choose construction to use


# descriptor state example
class DescState:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        del self.value


# client class
class CalcAttrs:
    X = DescState(2)
    Y = 3
    def __init__(self):
        self.Z = 4


# instance state example
class InstState:

    def __get__(self, instance, owner):
        return instance._X * 10

    def __set__(self, instance, value):
        instance._X = value

    def __delete__(self, instance):
        del instance._X

class CalcAttrs2:

    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z = 4


# mix of both conception
class DescBoth:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return ('{0}, {1}'.format(self.value, instance.value))

    def __set__(self, instance, value):
        instance.value = value

class Client3:
    def __init__(self, value):
        self.value = value
    managed = DescBoth('spam')


# ! Important: We can emulate property with descriptors
class Property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fset = fset
        self.fget = fget
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('cant get attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fset(instance, value)
    
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('cant delete attribute')
        self.fdel(instance)

class PersonProp:

    def getName(self):
        print('GetName...')

    def setName(self, valye):
        print('setName...')
    
    name = Property(getName, setName)


if __name__ == "__main__":
    
    X = Subject()
    X.attr
    Subject.attr


    X = C()
    X.a
    try:
        X.a = 99 # try ti set attribut, that readonly
    except AttributeError as a:
        print(a)

    # client outside version
    def testerOut(class_):
        print('='*30)
        bob = class_('Bob Smith')
        print(bob.name)
        bob.name = 'Robert Smith'
        print(bob.name)
        del bob.name
        print('-'*30)
        sue = class_('Sue Jons')
        print(sue.name)
        print(Name.__doc__) # or help(Name)
        print('='*30)

    testerOut(Person)

    # client inside version
    def testerIn(class_):
        print('='*30)
        bob = class_('Bob Smith')
        print(bob.name)
        bob.name = 'Robert Smith'
        print(bob.name)
        del bob.name
        print('-'*30)
        sue = class_('Sue Jons')
        print(sue.name)
        print(class_.Name.__doc__)
        print('='*30)

    testerIn(PersonIn)

c1 = Client1()
c2 = Client2()
print(c1.X, c2.X)
c1.X = 4
print(c1.X, c2.X)
del c1.X
try:
    print(c1.X)
except AttributeError as a:
    print(a)
print('='*30)


obj_ = CalcAttrs()
print(obj_.X, obj_.Y, obj_.Z) # Y, Z noncalculated
obj_.X = 5
CalcAttrs.Y = 6
obj_.X = 7
print(obj_.X, obj_.Y, obj_.Z)
obj_2 = CalcAttrs()
print(obj_2.X, obj_2.Y, obj_2.Z)
print('='*30)


obj_ = CalcAttrs2()
print(obj_.X, obj_.Y, obj_.Z) # Y, Z noncalculated
obj_.X = 5
CalcAttrs2.Y = 6
obj_.X = 7
print(obj_.X, obj_.Y, obj_.Z)
obj_2 = CalcAttrs2() # X is changed!
print(obj_2.X, obj_2.Y, obj_2.Z)
print('='*30)


I = Client3('eggs')
print(I.managed)
I.managed = 'SPAM'
print(I.managed)
print(I.__dict__)
print([x for x in dir(I) if not x.startswith('__')])
print(getattr(I, 'value'))
print(getattr(I, 'managed'))
for attr in (x for x in dir(I) if not x.startswith('__')):
    print('{0} => {1}'.format(attr, getattr(I, attr)))
print('='*30)


x = PersonProp()
x.name
x.name = 'Bob'
del x.name
