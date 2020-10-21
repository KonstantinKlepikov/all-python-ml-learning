# example of custom with\as manager construction

class TraceBlock:

    def message(self, arg):
        print('running ' + arg)

    def __enter__(self):

        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):

        if exc_type is None:
            print('normal exit\n')
        else:
            print('raise an exception' + str(exc_type))
            return False # propogation

if __name__ == "__main__":
    
    with TraceBlock() as action:
        action.message('test_1')
        print('complited')

    with TraceBlock() as action:
        action.message('test_2')
        raise TypeError
        print('not complited')

"""
starting with block
running test_1
complited
normal exit

starting with block
running test_2
raise an exception<class 'TypeError'>
Traceback (most recent call last):
File "with_as.py", line 29, in <module>
raise TypeError
TypeError
"""
