# example of class decoration mistakes

class Tracer:

    def __init__(self, aClass): # when decorate
        self.aClass = aClass # use instance attr

    def __call__(self, *args): # wen instance created
        self.wrapped = self.aClass(*args) # one instnce - LAST for eache class
        return self

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


if __name__ == "__main__":
    @Tracer # __init__ start
    class Spam: # Smap = Tracer(Spam)
        def display(self):
            print('Spam!' * 6)

    food = Spam() # start __call__
    food.display() # start __getattr__
    print('-'*20)

    # ! But we owerwrite al previous classes - becous we create
    # one instance per class, but storage only last instance of class
    @Tracer
    class Person:
        def __init__(self, name):
            self.name = name
    
    bob = Person('Bob')
    print(bob.name) # Bob
    sue = Person('Sue')
    print(sue.name) # Sue
    print(bob.name) # Sue
    print('-'*20)