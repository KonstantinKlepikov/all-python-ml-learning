class FirstClass:

    def setdata(self, value):
        self.data= value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):

    def display(self):
        print('Value of self.data is {0}'.format(self.data))

class ThirdClass(SecondClass):

    def __init__(self, value):
        # Вызывается для ThirdClass (value)
        self.data = value

    def __add__(self, other):
        # Вызывается для self + other
        return ThirdClass(self.data + other)

    def __str__(self):
        # Вызывается для print (sei f) , str()
        return 'ThirdClass: {0}'.format(self.data)

    def mul(self, other):
        # Изменеени е на месте - именованный метод
        self.data *= other
