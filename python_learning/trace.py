# example of delegation

class Wrapper:

    def __init__(self, obj):
        self.wrapped = obj # save object

    def __getattr__(self, attrname):
        print('Trace ' + attrname) # trace object
        return getattr(self.wrapped, attrname) # delegate extraction


if __name__ == "__main__":

    x = Wrapper([1, 2, 3]) # wrap list
    x.append(4) # delegate to list method
    print(x.wrapped) # print iside object

    x = Wrapper({'a': 1, 'b': 2}) # wrap dict
    list(x.keys()) # delegate to a list method