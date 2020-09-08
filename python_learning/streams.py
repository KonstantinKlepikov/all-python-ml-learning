# example of data streams

class Processor:
    """Define superclass
    """
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        """Process writing
        """
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        """Or generate exception
        """
        assert False, 'converter must be defined'

if __name__ == "__main__":

    class Uppercase(Processor):
        """Overloaded converter
        """
        def converter(self, data):
            return data.upper()

    import sys

    # simple case - read from file and use standart output
    Uppercase(open('content/spam.txt'), sys.stdout).process()

    # output to file
    Uppercase(open('content/spam.txt'), open('content/spum.txt', 'w')).process()

    # more dificult - output is interface with output method 
    # of class object
    class Htmlize:
        """Define writer as class
        """
        def write(self, line):
            print('<pre>{0}</pre>'.format(line.strip()))

    Uppercase(open('content/spam.txt'), Htmlize()).process()