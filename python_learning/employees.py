# example of inheritance

class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return '<Employee: name={0}, salary={1}'.format(
            self.name,
            self.salary
            )


class Chief(Employee):

    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):

    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chief):

    def __init__(self, name):
        Chief.__init__(self, name)

    def work(self):
        print(self.name, 'make pizza')


if __name__ == "__main__":

    bob = PizzaRobot('bob')
    print(bob) # run inherited method __repr__
    bob.work() # run specific method
    bob.giveRise(0.2) # run unherited method
    print(bob)
    print()

    for class_ in Employee, Chief, Server, PizzaRobot:
        obj = class_(class_.__name__)
        obj.work()
