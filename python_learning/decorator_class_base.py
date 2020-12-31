# basic example of class decorators

# singltone conception - one instance per class
instances = {}

def singletone(aClass): # when we define decorator before class
    def onCall(*args, **kwargs): # when we create instance
        if aClass not in instances: # one instance per class
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall


@singletone
class Person:

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singletone
class Spam:

    def __init__(self, val):
        self.val = val


# nonlocal version
def singletoneNonl(aClass): # when we define decorator before class
    instance = None
    def onCall(*args, **kwargs): # when we create instance
        nonlocal instance
        if instance == None: # one instance per class
            instance = aClass(*args, **kwargs)
        return instance
    return onCall


@singletoneNonl
class Person1:

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singletoneNonl
class Spam1:

    def __init__(self, val):
        self.val = val



if __name__ == "__main__":

    bob = Person('Bob', 40, 10)
    print(bob.name, bob.pay()) # Bob 400

    sue = Person('Sue', 50, 20)
    print(sue.name, sue.pay()) # Bob 400

    X = Spam(val=55)
    Y = Spam(150)
    print(X.val, Y.val) # 55 55
    print('-' * 50)

    bob = Person1('Bob', 40, 10)
    print(bob.name, bob.pay()) # Bob 400

    sue = Person1('Sue', 50, 20)
    print(sue.name, sue.pay()) # Bob 400

    X = Spam1(val=55)
    Y = Spam1(150)
    print(X.val, Y.val) # 55 55
    print('-' * 50)
