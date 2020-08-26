# documentation of class example


"I'm docstr.__doc__"


def dunc(args):
    "I'm docstr.func.__doc__"
    pass


class spam:
    "I'm spam.__doc__ or docstr.spam.__doc__ or self.__doc__"

    def method(self):
        "I'm spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)

