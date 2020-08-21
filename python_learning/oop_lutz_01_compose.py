# most realictic class example (with composite architecture)

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
        return 'Person: {0}, {1}, {2}'.format(self.name, self.job, self.pay)


class Manager(Person):
    """Inheritans
    """

    def __init__(self, name, pay):
        """In composite method we inject an exemplar of class Person 
        into class with constructor

        Args:
            name (str): 
            pay (int): 
        """

        self.person = Person(name, 'mng', pay)

    def giveRise(self, percent, bonus=.1):
        """We intersepr call of the attributes and delegate it
        to object self.person

        Args:
            percent (int): number with float to change pay definition
            bonus (int): number with float to change pay definition
        """

        self.person.giveRise(percent + bonus)

    def __getattr__(self, attr):
        """Delegate all other attributes

        Args:
            attr (obj):

        Returns:
            obj: attr
        """

        return getattr(self.person, attr)

    def __repr__(self):
        """We must reboot __repr__

        Returns:
            str: 
        """

        return str(self.person)


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

    # we domt use any value for attribute job, because it is define by class constructor
    tom = Manager('Tom Jones', 80000)
    tom.giveRise(.1)
    print(tom.lastName())
    print(tom)