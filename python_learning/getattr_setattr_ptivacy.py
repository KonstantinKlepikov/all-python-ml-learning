# example of usage __getattr__ and __setatr__ for privacy access to attributes

class PrivateExc(Exception):
    pass


class Privacy:
    """Example of definition attribute
    """

    def __setattr__(self, attrname, value):
        if attrname in self.privates: 
            raise PrivateExc(attrname, self) 
        else:
            self.__dict__[attrname] = value

class Usage1(PrivateExc):
    privates = ['age']

class Usage2(PrivateExc):

    privates = ['name', 'age']

    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':

    X = Usage1()
    Y = Usage2()

    X.name = 'Bob'
    print(X.name)

    # Y.name = 'Sue' # fail

    # X.age = 40 # fail
    Y.age = 30
    print(Y.age)
