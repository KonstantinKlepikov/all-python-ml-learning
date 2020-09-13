# example of multiple inheritans

class ListInherited:
    """Use dir() for collecting attributes and names
    of exemplar and inherited classes

    We uses __str__ insead of __repr__ for prevent infinite cicle
    """

    def __attrnames(self):
        result = ''
        for attr in dir(self): # dir() of exemplar
            if attr[:2] == '__' and attr[-2:] == '__': # exclude inside names
                result += '\t{0}\n'.format(attr)
            else:
                result += '\t{0}={1}\n'.format(attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of {0}, address {1}:\n{2}>'.format(
            self.__class__.__name__, # class name
            id(self), # address
            self.__attrnames() # list of name=value
            )


if __name__ == "__main__":

    import testmixin
    testmixin.tester(ListInherited)