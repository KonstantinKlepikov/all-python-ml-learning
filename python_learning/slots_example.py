# exmple of _slots__ usage

class Limiter:

    __slots__ = ['age', 'name', 'job'] # list of available attributes


class C:

    __slots__ = ['a', 'b'] # by default __slots__ mens that we havent __dict__


class D:

    __slots__ = ['a', 'b'] 

    def __init__(self):
        self.d = 4 # without __dict__ this definition is wrong


class E:

    __slots__ = ['a', 'b', '__dict__'] # define __dict__ for it including

    c = 3 # class attribute is fine

    def __init__(self):
        self.d = 4 # d is storaged in __dict__, but is a slot


# only last slots is visible, other is hidden
class First:

    __slots__ = ['c', 'd']

class Second(First):

    __slots__ = ['a', '__dict__']


class Slotful:

    __slots__ = ['a', 'b', '__dict__']

    def __init__(self, data):
        self.c = data


if __name__ == "__main__":

    x = Limiter()

    x.age = 40 # attribute must be defined befor is called
    print(x.age)

    try:
        print(x.name) # AttributeError: 'limiter' object has no attribute 'ape'
    except AttributeError:
        print('Attributeerror')

    z = C()
    z.a = 1
    print(z.a)

    try:
        print(x.name) # AttributeError: 'C' object has no attribute ’__diet__'
    except AttributeError:
        print('No __dict__')

    # but we can use __dict__ neutral methods
    print(getattr(z, 'a'))

    setattr(z, 'b', 2)
    print(z.b)

    print('a' in dir(z))
    print('b' in dir(z))

    try:
        y = D() # AttributeError: 'D’ object has no attribute ’d'
    except AttributeError:
        print('definition wrong')

    
    v = E()
    print(v.d) # 4
    print(v.c) # 3
    v.a = 2
    v.b = 1
    print(v.a, v.b) # 2, 1
    print(v.__dict__) # {'d': 4}
    print(v.__slots__) # {'a', 'b', '__dict__'}
    print(getattr(v, 'a'), getattr(v, 'c'), getattr(v, 'd')) # (1, 3, 4)


    fs = Second() # in exemplar we have all attributes (because __dict__), but not all slots
    fs.a = 1
    fs.b = 2
    fs.c = 3
    print(fs.a, fs.b, fs.c)
    print(First.__slots__) # [’с’, ’d’]
    print(Second.__slots__) # [’а', ’__diet__’]
    print(fs.__slots__) # [' а', '__dict__'] - inheritance last
    print(fs.__dict__) # {'Ь': 2}


    I = Slotful(3)
    I.a = 1
    I.b = 2
    print(I.a, I.b, I.c)
    print(I.__dict__)
