# example of exception conception, based on class

class General(Exception): 
    # inheritance from Exception not required in python 3.x, but isnt bad idea
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    X = General()
    raise X

def raiser1():
    X = Specific1()
    raise X

def raiser2():
    X = Specific2()
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General: # corresponds to superckass General and all subclasses
        import sys
        print('caught {}'.format(sys.exc_info()[0])) # caught very last exception by usage sys.exc_info()[0])

    """
    caught <class '__main__.General'>
    caught <class '__main__.Specific1'>
    caught <class '__main__.Specific2'>
    """

print('another solution')
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as X:
        print('caught {}'.format(X.__class__)) # in a __class__ we seen same, as in sys variant

    """
    caught <class '__main__.General'>
    caught <class '__main__.Specific1'>
    caught <class '__main__.Specific2'>
    """


if __name__ == "__main__":

    # we can create new subclass foк General and ершы цшдд
    # just expand top ctegory of exception
    
    class Specific3(General):
        pass
    

    print('error class extension')
    try:
        raise Specific3()
    except General:
        import sys
        print('caught {}'.format(sys.exc_info()[0]))

    """
    caught <class '__main__.Specific3'>
    """
