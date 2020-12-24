# comparison of property, descriptors, __getattr__ and __getattribute__

# property realisation
class PowersProp:

    def __init__(self, squire, cube):
        self._square = squire
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value
    
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube)


# descriptor realisation
class DescSquare:

    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:

    def __get__(self, instance, owner):
        return instance._cube ** 3

    def __set__(self, instance, value):
        instance._square = value


class PowersDesc:

    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


# __getattr__ realisation
class PowersGetattr:

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


# __getattrribute__ realisation
class PowersGetattribute:

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name) 

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value) 
        else:
            object.__setattr__(self, name, value) 


if __name__ == "__main__":

    def tested(X):
        print(X.square)
        print(X.cube)
        X.square = 5
        print(X.square)
        try:
            X.cube = 5
        except AttributeError as a:
            print(a)

    X = PowersProp(3, 4)
    tested(X)
    print('property' + '--' * 20)

    X = PowersDesc(3, 4)
    tested(X)
    print('descriptors' + '--' * 20)

    X = PowersGetattr(3, 4)
    tested(X)
    print('__getattr__' + '--' * 20)

    X = PowersGetattribute(3, 4)
    tested(X)
    print('__getattribute__' + '--' * 20)

