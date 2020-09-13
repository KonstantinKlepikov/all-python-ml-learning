# example of mixin class and multiple inheritance

from listinstance import ListInstance

class Main:

    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass

class Sub(Main, ListInstance): # mixin ham, and __str__

    def __init__(self):
        Main.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


if __name__ == "__main__":\

    X = Sub()
    print(X) # used a mixed method __str__