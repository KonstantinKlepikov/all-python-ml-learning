class AttrDisplay:
    """Give inheritated method for reboot. That method print
    exemplars of classes with it names and pair of name=value
    for each attribute, that are saved in that exemplar
    (this method cant reveal attributers, that are inherited 
    from classes). That class can be jonded to any classes and
    is ready to go in any exemplar
    """

    def gatherAttrs(self):

        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
