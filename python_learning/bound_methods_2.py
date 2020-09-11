# example of usage bound methods 
# as objects and with another objects


class Number:

    def __init__(self, num):
        self.num = num

    def double(self):
        return self.num * 2

    def tripple(self):
        return self.num * 3


# example of usage of other objects
def square(arg):
    return arg ** 2


class Sum:
    
    def __init__(self, num):
        self.num = num

    def __call__(self, arg):
        return self.num + arg

class Product:

    def __init__(self, num):
        self.num = num

    def method(self, arg):
        return self.num * arg

# classes is called objects to, but we call it for creating exemplars
class Negate:

    def __init__(self, num):
        self.num = -num

    def __repr__(self):
        return str(self.num)


if __name__ == "__main__":

    # objects of exemplars
    x = Number(2)
    y = Number(3)
    z = Number(4)

    print('normal direct: ' + str(x.double())) # normal direct calling

    acts = [x.double, y.double, z.tripple, y.tripple] # list of bound methods
    for act in acts:
        print(act()) # deffered call as function


    summ = Sum(2)
    prod = Product(3)
    acts = [square, summ, prod.method, Negate] # function, exemplar, bound method and class
    for act in acts: # no difference with calling
        print(act(5))

    print(acts[-2](55)) #indexing
    print([act(4) for act in acts]) # list including
    print(list(map(lambda act: act(7), acts))) # mapping
    table = {act(10): act for act in acts} # dict including
    for key, value in table.items():
        print('{0} => {1}'.format(key, value))
