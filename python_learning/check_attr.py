# example of checking attributes

#property version
class CardHolderProp():

    acctlen = 8
    retireage = 69.2

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else: self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value
    
    acct = property(getAcct, setAcct)

    def remainGet(self): # can be a method
        return self.retireage - self.age

    remain = property(remainGet)


# descriptors version


if __name__ == "__main__":

    def printholder(who):
        print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

    def tester(class_):
        bob = class_('1234-5678', 'Bob Smith', 40, '123 main str')
        printholder(bob)
        bob.name = 'Bob Q. Smith'
        bob.age = 50
        bob.acct = '23-45-67-89'
        printholder(bob)

        sue = class_('5678-12-34', 'Sue Jones', 35, '124 main str')
        printholder(sue)
        try: sue.age = 200
        except: print('bad age for')
        try: sue.remain = 5
        except: print('Cant set sremain')
        try: sue.acct = '1234567'
        except: print('wrong acct for')

    tester(CardHolderProp)

