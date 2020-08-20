# most realictic class example

class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        """Extract last name

        Returns:
            str: extracted last name
        """

        return self.name.split()[-1]

    def giveRise(self, percent):
        """Change pay definition

        Args:
            percent (int): number with float to change pay definition
        """

        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return 'Person: {0}, {1}'.format(self.name, self.pay)


if __name__ == "__main__":
    """Test for Person
    """

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay = 100000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())

    sue.giveRise(0.1)
    print(sue)