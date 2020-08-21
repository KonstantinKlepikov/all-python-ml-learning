# most realictic class example

from oop_lutz_01_classtools import AttrDisplay

class Person(AttrDisplay):

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


class Manager(Person):
    """Inheritans
    """

    def __init__(self, name, pay):
        """Redefine Person class constructor with new value of attribute job
        Calling method __init__ as class-method of parrent class
        with new value of attr job

        Args:
            name (str): 
            pay (int): 
        """

        Person.__init__(self, name, 'mng', pay)

    def giveRise_bad(self, percent, bonus=.1):
        """Example of bad solution of inheritans - ctrl-c ctrl-v code
        """

        self.pay = int(self.pay * (1 + percent + bonus))

    def giveRise(self, percent, bonus=.1):
        """Good example
        Redefinition with new attribute
        Calling method giveRise as class-method of parrent class
        Redefine self.pay

        Args:
            percent (int): number with float to change pay definition
            bonus (int): number with float to change pay definition
        """

        Person.giveRise(self, percent + bonus)


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