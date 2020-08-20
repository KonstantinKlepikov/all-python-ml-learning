class FirstClass:
    """Empty class
    """
    def setdata(self, value):
        """Class method

        Args:
            value (any type): example of class attribute
        """
        self.data= value

    def display(self):
        """Print class attribute
        """
        print(self.data)

class SecondClass(FirstClass):
    """Example of class inheritans
    """

    def display(self):
        """Redifinition of method, that print class attribute
        """
        print('Value of self.data is {0}'.format(self.data))

class ThirdClass(SecondClass):
    """Example of class inheritans
    """
    def __init__(self, value):
        """Example of class constructor

        Args:
            value (any type): example
        """
        self.data = value

    def __add__(self, other):
        """Redifinition of operathor +

        Args:
            other (any type): example

        Returns:
            object: exemplar of ThirdClass
        """
        return ThirdClass(self.data + other)

    def __str__(self):
        """Difinition for print(seif)

        Returns:
            str: information about class attribute
        """
        return 'ThirdClass: {0}'.format(self.data)

    def mul(self, other):
        """Changes in place - example of named method

        Args:
            other (any type): example
        """
        self.data *= other
