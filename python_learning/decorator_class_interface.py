# example of interface tracking with decorators

def Tracer(aClass): # whe use decorarator

    class Wrapper:

        def __init__(self, *args, **kwargs): # when make instance
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, attrname):
            print('Trace: ' + attrname) # all attribute except own
            self.fetches += 1
            return getattr(self.wrapped, attrname) # delegated to inside object

    return Wrapper


if __name__ == "__main__":

    @Tracer
    class Spam:

        def display(self):
            print('Spam!' * 8)


    @Tracer
    class Person:

        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        def pay(self):
            return self.hours * self.rate

    food = Spam()
    food.display()
    print([food.fetches])
    # Trace: display
    # Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
    # [1]

    bob = Person('Bob', 40, 10)
    print(bob.name, bob.pay())
    # Trace: name
    # Trace: pay
    # Bob 400

    sue = Person('Sue', 50, 20)
    print(sue.name, sue.pay())
    # Trace: name
    # Trace: pay
    # Sue 1000

    print(bob.name, bob.pay())
    print([bob.fetches, sue.fetches])
    # Trace: name
    # Trace: pay
    # Bob 400
    # [4, 2]
    print('-'*20)

    # build-in types decoration
    # we need wrap build-in objects or create subclass, because @ sintax wait fo class type
    
    # subclass usage
    @Tracer
    class MyList(list): 
        pass

    x = MyList([1, 2, 3])
    x.append(4)
    print(x.wrapped)
    # Trace: append
    # [1, 2, 3, 4]

    # handmade decoration
    WrapList = Tracer(list)
    x = WrapList([4, 5, 6])
    x.append(7)
    print(x.wrapped)
    # Trace: append
    # [4, 5, 6, 7]
