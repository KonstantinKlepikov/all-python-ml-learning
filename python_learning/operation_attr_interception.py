# example of attribute interception for intain operation

class GetAttr:

    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:

    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattribute str]'
        else:
            return lambda *args: None


if __name__ == "__main__":

    for class_ in GetAttr, GetAttribute:
        print('\n' + class_.__name__.ljust(50, '='))
        X = class_()
        X.eggs
        X.spam
        X.other
        len(X)

        try: X[0] # ? __getitem__
        except: print('fail []')

        try: X + 99 # ? __add__
        except: print('fail +')

        try: X() # ? __call__
        except: print('fail ()')

        X.__call__()
        print(X.__str__())
        print(X)