# private and public conceptions for decorators and closed attributes

traceMe = False

def trace(*args): # code for selftesting
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):

    def onDecorator(aClass):

        class onInstance:

            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get: ', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set: ', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)

        return onInstance

    return onDecorator

def Private(*attributres):
    return accessControl(failIf=(lambda attr: attr in attributres))

def Public(*attributres):
    return accessControl(failIf=(lambda attr: attr not in attributres))


if __name__ == "__main__":

    @Private('age')
    class Person1:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    X = Person1('Bob', 40)
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        print(X.age)
    except TypeError as a:
        print(a)

    @Public('name')
    class Person2:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    X = Person2('Bob', 40)
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        print(X.age)
    except TypeError as a:
        print(a)
