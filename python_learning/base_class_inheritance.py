# example of extending 
# by class creation as base class child


class Set(list):

    def __init__(self, value = []): # poor solution
        list.__init__(self)
        self.concat(value)

    def intersect(self, other):
        """Intersection method

        Args:
            other (obj): any sequence

        Returns:
            obj: class Set() exemplar
        """
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        """Union method

        Args:
            other (obj): any sequence

        Returns:
            obj: class Set() exemplar
        """
        res = Set(self)# copy of list
        res.concat(other)
        return res

    def concat(self, value):
        """Concatination method

        Args:
            value (obj): any sequence
        """
        for x in value: # dedublication
            if not x in self:
                self.append(x)

    def __and__(self, other):
        # self & other
        return self.intersect(other)

    def __or__(self, other):
        # self | otegr
        return self.union(other)

    def __repr__(self):
        # print(self)
        return 'Set:' + list.__repr__(self)


if __name__ == "__main__":

    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7]))) # Set:[1, 3, 5, 7, 4]
    print(x | Set([1, 4, 6])) # Set:[1, 3, 5, 7, 4, 6]
