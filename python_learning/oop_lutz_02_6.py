""" Example of ascend in inheritance tree with visualisation
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)

    # call in recursion for all cls
    for superclass in cls.__bases__:
        classtree(superclass, indent + 3)


def instancetree(inst):
    print('Tree of {}'.format(inst)) #shown exemplar
    classtree(inst.__class__, 3) # ascend in it class


def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    instancetree(F())


if __name__ == '__main__':
    selftest() 
