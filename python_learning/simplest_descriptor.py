# example of descriptor conception

class AgeDesk:

    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class Descriptors:
    age = AgeDesk()


if __name__ == "__main__":

    x = Descriptors()

    print(x.age) # start AgeDesc.__get__
    x.age = 42 # start AgeDesc.__set__
    print(x._age) # normal usage (without AgeDesc)