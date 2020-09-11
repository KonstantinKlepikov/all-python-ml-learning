# example of bound and unbound methods

class Spam:

    def doit(self, message):
        print(message)


obj = Spam()

obj.doit('Hello world') # bound (self is added)

x = obj.doit
x('Hello world') # another example

# same is tru for methods inside class
class Eggs:
    def one(self, n):
        print(n)
    def two(self):
        x = self.one
        x(42)
Eggs().two()

# object of unbound method (term is excluded since python 3.X)
# now is calling as "simple function"
y = Spam.doit
y(obj, 'What was that') # give an exemplar to a a method


# simple function and bound method inside class python 3.X
class Selfless:

    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2): # simple function
        print(arg1 + arg2)

    def normal(self, arg1, arg2): # bound method (it waiting exemplar, when called)
        print(self.data + arg1 + arg2)

z = Selfless(2)
Selfless.normal(z, 3, 4) # handed
z.normal(3, 4) # auto
Selfless.selfless(3, 4) #simple function (with no exemplar)