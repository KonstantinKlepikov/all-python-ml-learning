# example of metaclass - basic terms

class MetaOne(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)


class MetaTwo(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(class_, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
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

    class Spam2(Eggs, metaclass=MetaTwo):
        data = 1
        def meth(self, arg):
            return self.data + arg

    print('Make instance')
    Y = Spam2()
    print('data:', Y.data, Y.meth(2))
