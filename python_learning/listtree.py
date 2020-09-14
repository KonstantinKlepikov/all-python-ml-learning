# example of multiple inheritans

class ListTree:
    """Mixin class ,that return in __str__ result tree of inherited classes
    and attributes of all objects, since of self and higher
        
    print() or str() retuen bult-in string

    ames __X prevents conflicts with attributes of client
    """

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'): # exclude inside names
                result += '\t{0}\n'.format(attr)
            else:
                result += '\t{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, class_, indent):
        dots = '.' * indent
        if class_ in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                class_.__name__,
                id(class_)
            )
        else:
            self.__visited[class_] = True
            here = self.__attrnames(class_, indent)
            above = ''
            for main in class_.__bases__:
                above += self.__listclass(main, indent + 4)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                class_.__name__,
                id(class_),
                here,
                above,
                dots
            )

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__, # class name
            id(self), # address
            here,
            above
            )


if __name__ == "__main__":

    import testmixin
    testmixin.tester(ListTree)