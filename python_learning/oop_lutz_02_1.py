# Example of methodics of class binding

class Parrent:
    """Superclass
    """

    def method(self):
        print('In Parrent.method') # standard behavor

    def delegate(self):
        self.action() # expected of method definition in subclass
    
    def action(self):
        assert False, 'action not defined' # if called this version


class Inheritor(Parrent):
    """Simple inherit
    """
    pass


class Replacer(Parrent):
    """Redefine method from Parrent
    """

    def method(self):
        print('In Replacer.method')


class Extender(Parrent):
    """Replace and call for original method
    """

    def method(self):
        print('Starting Extender.method')
        Parrent.method(self)
        print('Ending Extender.method')


class Provider(Parrent):
    """Define action for Parrent.delegate()
    """

    def action(self):
        print('In Provider.method')


if __name__ == '__main__':

    for class_ in (Inheritor, Replacer, Extender):
        print('\n' + class_.__name__ + '...')
        class_().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    
    # example of call undefined method from abstract superclass
    X = Parrent()
    X.delegate() 
    # in Python 3.X we can use from abc import ABCMeta, abstractmethod
    # for abstract superclass. In that realisation we cant create exemplars
    # for as long in subclass not realise all abstract methods