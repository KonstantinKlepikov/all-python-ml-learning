# example of composition

from employees import PizzaRobot, Server

class Customer:

    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, ' orders from ', server)

    def pay(self, server):
        print(self.name, ' pays for item to ', server)

    
class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    """Inception and activation of other objects
    """
    def __init__(self):
        # inception
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        # activation
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":

    scene = PizzaShop() # composited object
    scene.order('Homer') # create of order
    print('.'*10)
    scene.order('Shaggy') # create of order
    print('.'*10)