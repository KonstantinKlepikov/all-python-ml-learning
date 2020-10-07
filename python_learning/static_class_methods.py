# example of static and class methods and alternatives

"""Alternative solution for static methods 
to counts of number of exemplars - outside function"""

def printNumInstances():
    print('Number of created instances: {0}'.format(Spam.numInstances))

class Spam:

    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

# main example of methods
class Methods:

    def imeth(self, x): # exemplar method
        print([self, x])

    @staticmethod # not gets self
    def smeth(x):
        print(x)

    @classmethod # gets cls instead of self
    def cmeth(cls, x):
        print([cls, x])

"""Count of exemplars by static methods
"""

class SpamStat:

    numInstances = 0

    def __init__(self):
        SpamStat.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of created instances: {0}'.format(SpamStat.numInstances))


class Sub(SpamStat): # with static method we can realise inheritance

    @staticmethod
    def printNumInstances():
        print('Extrastuff...')
        SpamStat.printNumInstances()


class Other(SpamStat): # inheritance without redefinition
    pass

"""Count of exemplars by class method
"""
class SpamCls:

    numInstances = 0

    def __init__(self):
        SpamCls.numInstances = SpamCls.numInstances + 1

    @classmethod
    def printNumInstances(cls):
        print('Number of created instances: {0} {1}'.format(cls.numInstances, cls))


class SubCls(SpamCls):

    @classmethod
    def printNumInstances(cls):
        print('Extrastuff...', cls)
        SpamCls.printNumInstances()


class OtherCls(SpamCls):

    pass


if __name__ == "__main__":

    a = Spam()
    b = Spam()
    c = Spam()

    printNumInstances() # can't be inherited


    # tree types of methods

    # standard or exemplar method
    X = Methods() # calling from exemplar or class
    X.imeth(1)
    Methods.imeth(X, 2)

    # static method - called by exemplar or class without self
    Methods.smeth(3)
    X.smeth(4)

    # class method - cls instead of self
    Methods.cmeth(5)
    X.cmeth(6)


    # count with staticmethod
    a = SpamStat()
    b = SpamStat()
    c = SpamStat()
    SpamStat.printNumInstances() # called as simple function
    a.printNumInstances() # without self

    d = Sub() # inheritance
    Sub.printNumInstances()
    d.printNumInstances()
    SpamStat.printNumInstances()

    e = Other() # without redefinition of classmethod
    e.printNumInstances()


    # count with classmethod
    a = SpamCls()
    b = SpamCls()
    a.printNumInstances()
    SpamCls.printNumInstances()

    # attention - classmethod gets only last class
    x = SpamCls()
    z = SubCls()    
    z.printNumInstances()
    # Extrastuff... <class '__main__.SubCls'>
    # 4 <class '__main__.SpamCls'>

    SubCls.printNumInstances()
    # Extrastuff... <class '__main__.SubCls'>
    # 4 <class '__main__.SpamCls'>

    x.printNumInstances() 
    # 4 <class '__main__.SpamCls'>

    c = OtherCls()
    c.printNumInstances() 
    # 5 <class '__main__.OtherCls'>
