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