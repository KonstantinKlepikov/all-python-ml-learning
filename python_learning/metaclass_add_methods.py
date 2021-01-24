# example of adding methods with metaclass

# this new methods
def eggfunc(that):

    return that.value * 4


def hamfunc(that, value):

    return value + 'ham'


# realisation without metaclasses
class Client1:

    def __init__(self, value):
        self.value = value
    
    def spam(self):
        return self.value * 2


class Client2:

    value = 'this'


Client1.eggs = eggfunc
Client1.ham = hamfunc

Client2.eggs = eggfunc
Client2.ham = hamfunc


# realisation with metaclass
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


# solution with decorators
def ExtenderD(aClass):

    aClass.eggs = eggfunc
    aClass.ham = hamfunc
    return aClass


@ExtenderD
class Client1d:

    def __init__(self, value):
        self.value = value
    
    def spam(self):
        return self.value * 2


@ExtenderD
class Client2d:

    value = 'this'


if __name__ == '__main__':

    # realisation without metaclasses
    X = Client1('THIS')
    print(X.spam(), X.eggs(), X.ham('beacon'))

    Y = Client2()
    print(Y.eggs(), Y.ham('beacon'))

    # realisation with metaclass
    XX = Client1s('THIS')
    print(XX.spam(), XX.eggs(), XX.ham('beacon'))

    YY = Client2s()
    print(YY.eggs(), YY.ham('beacon'))

    # solution with decorators
    XXX = Client1d('THIS')
    print(XXX.spam(), XXX.eggs(), XXX.ham('beacon'))

    YYY = Client2d()
    print(YYY.eggs(), YYY.ham('beacon'))
