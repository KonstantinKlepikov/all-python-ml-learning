# example of realisation of decorator function and class attr
# we close access to that attrs otside of class

traceMe = False

def trace(*args): # code for selftesting
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):

    def onDecorator(aClass):

        class onInstance: # in attr of instance

            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr): # dont use for self attr of decorator
                trace('get: ', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set: ', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value # no infinite looping
                elif attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return onInstance

    return onDecorator


if __name__ == "__main__":
    traceMe = True

    @Private('data', 'size') # Doubler = Private(...)(Doubler)
    class Doubler:
        
        def __init__(self, label, start):
            self.label = label # we can use this operation only inside of class
            self.data = start

        def size(self):
            return len(self.data) # class method can be used outside of class

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        
        def display(self):
            print('{0} => {1}'.format(self.label, self.data))


    X = Doubler('X is', [1, 2, 3]) # [set: wrapped<__main__.Doubler object at 0x7fd8c52d5c10>]
    print('-'*10)

    # intercept, check and delegate
    print(X.label) 
    # [get: label]
    # X is
    print('-'*10)

    X.display()
    # [get: display]
    # X is => [1, 2, 3]
    print('-'*10)

    X.double()
    # [get: double]
    print('-'*10)

    X.label = 'Spam'
    # [set: labelSpam]
    print('-'*10)

    X.display()
    # [get: display]
    # Spam => [2, 4, 6]
    print('-'*10)

    try:
        print(X.size())
    except TypeError as a:
        print(a)
    # [get:  size]
    # private attribute fetch: size

    try:
        print(X.data)
    except TypeError as a:
        print(a)
    # [get:  data]
    # private attribute fetch: data

    try:
        X.data = [1, 1, 1]
    except TypeError as a:
        print(a)
    # [set:  data [1, 1, 1]]
    # private attribute fetch: data

    try:
        X.size = lambda S: 0
    except TypeError as a:
        print(a)
    # [set:  size <function <lambda> at 0x7f62784e9170>]
    # private attribute fetch: size