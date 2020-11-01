# overloading __call__

class Prod:
    """Example of save attr when create exemplar
    """

    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


class Callback:
    """Callback example
    """

    def __init__(self, color): # function and information for future
        self.color = color

    def __call__(self): # call with no arguments
        print('turn', self.color)


if __name__ == "__main__":
    x = Prod(2)
    print(x(3)) # 6
    print(x(4)) # 8

    #callback
    cb1 = Callback('blue')
    cb2 = Callback('red')

    cb1()
    cb2()

    # alternative 1
    def callback(color):
        def onecall():
            print('turn', color)
        return onecall

    cb3 = callback('green')
    cb3()

    # alternative 2
    cb4 = (lambda  color = 'black': 'turn ' + color)
    print(cb4()) # look at syntaxis


    # alternative 3
    class Callback_met:
        """Example with linked method
        """

        def __init__(self, color):
            self.color = color

        def changeColor(self): # clinked method
            print('turn', self.color)

    cb5 = Callback_met('yellow')
    obj = cb5.changeColor
    obj() # look at syntaxis
