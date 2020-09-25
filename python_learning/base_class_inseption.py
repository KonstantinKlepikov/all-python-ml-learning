# example of extending of types with inseption


class Set:

    def __init__(self, value = []): # poor solution
        self.data = []
        self.concat(value)

    def intersect(self, other):
        """Intersection method

        Args:
            other (obj): any sequence

        Returns:
            obj: class Set() exemplar
        """
        res = []
        for x in self.data:
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
        res = self.data[:] # copy of list
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        """Concatination method

        Args:
            value (obj): any sequence
        """
        for x in value: # dedublication
            if not x in self.data:
                self.data.append(x)

    # inseption
    def __len__(self):
        # len(self) if self is True
        return len(self.data)
    
    def __getitem__(self, key):
        # self[i], self[i,j]
        return self.data[key]

    def __and__(self, other):
        # self & other
        return self.intersect(other)

    def __or__(self, other):
        # self | otegr
        return self.union(other)

    def __repr__(self):
        # print(self)
        return 'Set:' + repr(self.data)

    def __iter__(self):
        # for x in self
        return iter(self.data)


if __name__ == "__main__":

    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7]))) # Set:[1, 3, 5, 7, 4]
    print(x | Set([1, 4, 6])) # Set:[1, 3, 5, 7, 4, 6]
