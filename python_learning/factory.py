# simple example of factory principles

def factory_(class_, *args, **kwargs):

    return class_(*args, **kwargs)

class Spam:

    def doit(self, message):
        print(message)

class Person:

    def __init__(self, name, job=None):
        self.name = name
        self.job = job


if __name__ == "__main__":

    obj1 = factory_(Spam)
    obj2 = factory_(Person, 'Maria', 'Stuart')
    obj3 = factory_(Person, name='Elizabeth')

    obj1.doit('Oops!')
    print(obj2.name, obj2.job)
    print(obj3.name, obj3.job)