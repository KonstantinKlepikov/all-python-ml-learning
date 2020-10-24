# example of redefinition __init__

class FormatError(Exception): # redifine __init__ of Exception for add more information

    def __init__(self, line, files):
        self.line = line
        self.files = files


def parser():
    raise FormatError(42, files='spam.txt')


try:
    parser()
except FormatError as X:
    print('Error at: {0} line {1}'.format(X.files, X.line))
