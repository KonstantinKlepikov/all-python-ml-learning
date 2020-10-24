# example of redefinition __repr__ and __str__ of exception

class MyBad(Exception):

    def __str__(self):
        return 'My mistake!'


class MyBad2(Exception):

    def __repr__(self):
        return 'Not calable' # because buid-in method has __str__


try:
    raise MyBad('spam')
except MyBad as X:
    print(X) # My mistake!
    print(X.args) # ('spam',)

try:
    raise MyBad2('spam')
except MyBad2 as X:
    print(X) # spam
    print(X.args) # ('spam',)

raise MyBad('spam') # __main__.MyBad2: My mistake!
# raise MyBad2('spam') # __main__.MyBad2: spam 