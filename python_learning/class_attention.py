# example of traps of class construction

"""Chenging of class attributes can have side effect
"""
class X:
    a = 1


"""Chenging of modified attributes can have side effect to
"""
class C:
    shared = []
    def __init__(self):
        self.perobj = []


"""Area of visibility in methods and classes
"""
def generate1():
    class Spam: # Spam - name for local area of generate()
        count = 1
        def method(self):
            print(Spam.count)
    return Spam()


def generate2():
    return Spam1()

class Spam1: # is in top level of module
    count = 2
    def method(self):
        print(Spam1.count)


def generate3(label): # return class instead of exemplar
    class Spam:
        count = 3
        def method(self):
            print('{0}={1}'.format(label, Spam.count))
    return Spam


if __name__ == "__main__":
    I = X()
    print(I.a)
    print(X.a)
    print('side effect')
    X.a = 2
    print(I.a)
    J = X()
    print(J.a) # and in that exemplar to

    x = C()
    y = C()
    print(y.shared, y.perobj) # ([], [])
    x.shared.append('spam') # is translated to class attr in C()
    x.perobj.append('spam') # is actual only in class exemplar
    print(x.shared, x.perobj) # (['spam'], ['spam'])
    print(y.shared, y.perobj) # (['spam'], [])
    print(C.shared) # ['spam]

    generate1().method() # 1
    generate2().method() # 2
    a = generate3('WhoIAm')
    a().method() # WhoIAm' = 3
