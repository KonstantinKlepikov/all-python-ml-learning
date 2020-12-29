# fabric method for decorators (isnt best idea)

from abc import ABC, abstractmethod


class Fabricator(ABC):

    @classmethod
    @abstractmethod
    def is_check_for(cls, check):
        pass

    @abstractmethod
    def do_something(self):
        pass


class Product1(Fabricator):

    @classmethod
    def is_check_for(cls, check):
        return check == 1

    def do_something(self):
        print('Now im in Product1')


class Product2(Fabricator):

    @classmethod
    def is_check_for(cls, check):
        return check == 2

    def do_something(self):
        print('Now im in Product2')

class tracker:
    """Im tracker docstring
    """

    def __init__(self, function):
        self.function = function

    def __call__(self, check, *args):
        for cls_ in Fabricator.__subclasses__():
            if cls_.is_check_for(check):
                cls_().do_something()
        self.function(check, *args)


@tracker
def tester(check, a, b):
    """Im tester docstring
    """

    print('Sum is: ', a + b)


if __name__ == "__main__":

    for i in 1, 2:
        tester(i, 1, 2)
    
    print(tester.__doc__)
