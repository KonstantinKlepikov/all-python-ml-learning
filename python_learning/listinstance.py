# example of multiple inheritans

class ListInstance:
    """Mixin class, that define formated function print()
    or str() for examplars. This is provided by inheritance
    of method __str__. Displays only attributes of examplars.
    Self is an exemplar of most last class.

    Names __X prevents conflicts with attributes of client
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t{0}={1}\n'.format(attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of {0}, address {1}:\n{2}>'.format(
            self.__class__.__name__, # class name
            id(self), # address
            self.__attrnames() # list of name=value
            )


if __name__ == "__main__":

    import testmixin
    testmixin.tester(ListInstance)