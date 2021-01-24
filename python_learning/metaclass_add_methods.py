# example of adding methods with metaclass

# without metaclasses
class Client1:

    def __init__(self, value):
        self.value = value
    
    def spam(self):
        return self.value * 2


class Client2:

    value = 'this'


def eggfunc(that):

    return that.value * 4


def hamfunc(that, value):

    return value + 'ham'


Client1.eggs = eggfunc
Client1.ham = hamfunc

Client2.eggs = eggfunc
Client2.ham = hamfunc


# metaclass realisation
class Extender(type):

    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


class Client1s(metaclass=Extender):

    def __init__(self, value):
        self.value = value
    
    def spam(self):
        return self.value * 2


class Client2s(metaclass=Extender):

    value = 'this'


if __name__ == '__main__':

    X = Client1('THIS')
    print(X.spam(), X.eggs(), X.ham('beacon'))

    Y = Client2()
    print(Y.eggs(), Y.ham('beacon'))

    XX = Client1s('THIS')
    print(XX.spam(), XX.eggs(), XX.ham('beacon'))

    YY = Client2s()
    print(YY.eggs(), YY.ham('beacon'))
