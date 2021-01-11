# example of decorators usage for managing of function and classes

registry = {}
def register(obj):
    registry[obj.__name__] = obj # add to register
    return obj # return an object, not a wrapper

@register
def spam(x):
    return x ** 2

@register
def ham(x):
    return x ** 3

@register
class Eggs:

    def __init__(self, x):
        self.data = x ** 4
    
    def __str__(self):
        return str(self.data)


def decorate(func):
    func.marked = True # new attr for function
    return func

@decorate
def this(a, b):
    return a + b

def annotate(text): # same, as previous, but value is an argument of decorator
    def decorate(func):
        func.label = text
        return func
    return decorate

@annotate('spam data')
def that(a, b):
    return a + b


if __name__ == "__main__":
    print('Registry:')

    for name in registry: # What is in register
        print(name, '=>', registry[name], type(registry[name]))
        # spam => <function spam at 0x7f61586ce320> <class 'function'>
        # ham => <function ham at 0x7f61586d2d40> <class 'function'>
        # Eggs => <class '__main__.Eggs'> <class 'type'>

    print('\nManual calls:') # call objects manualy
    print(spam(2), ham(2)) # 4 8
    X = Eggs(2)
    print(X) # 16

    print('\nRegister calls:') #calls from register
    for name in registry:
        print(name, '=>', registry[name](2))
        # spam => 4
        # ham => 8
        # Eggs => 16


    print(this.marked) # True
    print(that(1, 2), that.label) # 3 'that data'
