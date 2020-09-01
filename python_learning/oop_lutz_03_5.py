# example of usage __getattr__ and __setatr__ for access to attributes

class Empty:
    """Example of link to attribute
    """

    def __getattr__(self, attrname): #for undefined attr in self

        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

class AccessControl:
    """Example of definition attribute
    """

    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10 
            # cant be self.attr = value or setattr, for reason infinite cycle
            # insted we use definition afor key of dict 
        else:
            raise AttributeError(attr + ' not allowed')

X = Empty()
print(X.age)
# X.name

Y = AccessControl()
Y.age = 40
print(Y.age)
# Y.name