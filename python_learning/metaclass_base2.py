class MetaOne(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'


class MetaSuper(metaclass=MetaOne):

    def spam(self):
        return 'spam'


class MetaSub(MetaSuper):

    def eggs(self):
        return 'eegs'


if __name__ == '__main__':

    X = MetaSub()
    print(X.eggs()) # inherited from MetaSub

    print(X.spam()) # inherited from MetaSuper

    try:
        print(X.toast()) # not inherited from metaclass
    except AttributeError as a:
        print(a)

    print(X.spam)
    print(MetaSub.toast)
    print(MetaSub.spam)
