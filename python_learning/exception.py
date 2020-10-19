# Examples of exceptions

def fetcher(obj, index):
    return obj[index]


class AlreadyGotOne(Exception):
    pass


def grail():
    raise AlreadyGotOne()


if __name__ == "__main__":
    x = 'spam'
    print(fetcher(x, 3)) # 'm'

    # catching exceptions
    def catcher():
        # IndexError: string index out of range
        try:
            print(fetcher(x, 4))
        except IndexError:
            print('string index out of range')
        print('continuing')

    catcher()

    # generating exception
    try:
        raise IndexError
    except IndexError:
        print('Raised: string index out of range')

    # define exception
    try:
        grail()
    except AlreadyGotOne:
        print('AlreadyGotOne exception')

    
    # finaly
    try:
        fetcher(x, 3)
    finally:
        print('is done even if no exception')

    def after():
        try:
            fetcher(x, 4)
        finally:
            print('or if excepted')
        print('but no after') # is dont, because finally is resolved before exception and exception next

    after()
