# example of metaclass - basic terms

# redefine __new__
class MetaOne(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)


# both __new__ and __init__
class MetaTwo(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(class_, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(class_.__dict__.keys()))


# we can use both or any classmethods to define metaclass:
# just redefine __new__ or/and __init__ of type superclass

# fabric function as metaclass
def MetaFunc(classname, supers, classdict):
        print('In Metafunc:', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

# exemplar of normal class (overload call operation with nor,al calls)
# we uses Init and New for methods to prevent run self init and new
class MetaObj:

    def __call__(self, classname, supers, classdict):
        print('In MetaObj:', classname, supers, classdict, sep='\n...')
        class_ = self.__New__(classname, supers, classdict)
        self.__Init__(class_, classname, supers, classdict)
        return class_
    
    def __New__(self, classname, supers, classdict):
        print('In MetaObj.New:', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, class_, classname, supers, classdict):
        print('In MetaObj.Init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(class_.__dict__.keys()))


# and same from superclass (but is it's not obvious)
class SuperMetaObj:

    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj:', classname, supers, classdict, sep='\n...')
        class_ = self.__New__(classname, supers, classdict)
        self.__Init__(class_, classname, supers, classdict)
        return class_
    
    def __New__(self, classname, supers, classdict):
        print('In SuperMetaObj.New:', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, class_, classname, supers, classdict):
        print('In SuperMetaObj.Init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(class_.__dict__.keys()))


# overload call operations with metaclasses
class SuperMeta(type):

    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta:', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)

    def __init__(class_, classname, supers, classdict):
        print('In SuperMeta.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(class_.__dict__.keys()))


class SubMeta(type, metaclass=SuperMeta): # making metaclass

    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(class_, classname, supers, classdict):
        print('In SubMeta.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(class_.__dict__.keys()))


class Eggs:
    pass


if __name__ == "__main__":

    print('Making class')
    class Spam1(Eggs, metaclass=MetaOne):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    X = Spam1()
    print('data:', X.data, X.meth(2))
    print('='*20)


    print('Making class')
    class Spam2(Eggs, metaclass=MetaTwo):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    Y = Spam2()
    print('data:', Y.data, Y.meth(2))
    print('='*20)


    print('Making class')
    class Spam3(Eggs, metaclass=MetaFunc):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    Z = Spam3()
    print('data:', Z.data, Z.meth(2))
    print('='*20)


    print('Making class')
    class Spam4(Eggs, metaclass=MetaObj()):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    A = Spam4()
    print('data:', A.data, A.meth(2))
    print('='*20)


    print('Making class')
    class Spam5(Eggs, metaclass=SuperMetaObj()):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    B = Spam5()
    print('data:', B.data, B.meth(2))
    print('='*20)


    print('Making class')
    class Spam6(Eggs, metaclass=SubMeta):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    C = Spam6()
    print('data:', C.data, C.meth(2))
