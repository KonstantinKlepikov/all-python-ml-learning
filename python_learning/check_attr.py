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


# descriptors version (1 variant - separated statement of instance)
class CardHolderDesc1():

    acctlen = 8
    retireage = 69.2

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr


    class Name:


        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value

    name = Name()
    

    class Age:

        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else: self.age = value

    age = Age()


    class Acct:

        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value
    
    acct = Acct()


    class Remain:

        def __get__(self, instance, owner):
            return instance.retireage - instance.age # Age.__get__ is started

        def __set__(self, instance, value):
            raise TypeError('Cannot set remain')

    remain = Remain()

# descriptors version (2 variant - statemente for each instance)
class CardHolderDesc2():

    acctlen = 8
    retireage = 69.2

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr


    class Name:


        def __get__(self, instance, owner):
            return instance.__name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value

    name = Name()
    

    class Age:

        def __get__(self, instance, owner):
            return instance.__age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else: instance.__age = value

    age = Age()


    class Acct:

        def __get__(self, instance, owner):
            return instance.__acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                instance.__acct = value
    
    acct = Acct()


    class Remain:

        def __get__(self, instance, owner):
            return instance.retireage - instance.age # Age.__get__ is started

        def __set__(self, instance, value):
            raise TypeError('Cannot set remain')

    remain = Remain()


# __getattr__ version
class CardHolderGetattr():

    acctlen = 8
    retireage = 69.2

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:-3] + '***'
        elif name == 'remain':
            return self.retireage - self.age # dont start __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':            
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('Cannot set remain')
        self.__dict__[name] = value # prevent infinite cycling


# __getattribute__ version
class CardHolderGetattribute():

    acctlen = 8
    retireage = 69.2

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattribute__(self, name):
        superget = object.__getattribute__ # prevent infinite cycling

        if name == 'acct':
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)

    def __setattr__(self, name, value):
        if name == 'name':            
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('Cannot set remain')
        self.__dict__[name] = value # prevent infinite cycling


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

        print('='*50)

    print('Property ->')
    tester(CardHolderProp)

    print('Descriptor ver.1 ->')
    tester(CardHolderDesc1)

    print('Descriptor ver.2 ->')
    tester(CardHolderDesc2)

    print('__getattr__ ->')
    tester(CardHolderGetattr)

    print('__getattribute__ ->')
    tester(CardHolderGetattribute)
