# example of mixin class and multiple inheritance

"""This is a instrument for testing mixed classes for 
printing of lists
"""

import importlib


def tester (listerclass, sept=False):

    class Main:

        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Main, listerclass): # class for inherit is defined when function called

        def __init__(self):
            Main.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()

    print(instance)

    if sept:
        print('-' * 80)

def testByNames(modname, classname, sept=False):

    modobj = importlib.import_module(modname) # import by string name
    listerclass = getattr(modobj, classname) # attr by string methods
    tester(listerclass, sept)


if __name__ == "__main__":

    testByNames('listinstance', 'ListInstance', True)
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)