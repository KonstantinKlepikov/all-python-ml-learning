# example of definitions of names part 3

#global name
X = 11

# access to global name from function
def f():
    if __name__ == '__main__':
        print(X)

# changing global name X in module
def g():
    global X
    X = 22
    if __name__ == '__main__':
        print(X)

def h1():
    X = 33 # locale name in function
    def nested():
        print(X) # link to local name
    if __name__ == '__main__':
        nested()

def h2():
    X = 33 # locale name in function
    def nested():
        nonlocal X 
        X = 44
        print(X)
    if __name__ == '__main__':
        nested()
    print(X)


if __name__ == '__main__':
    print(X) # 11
    f() # 11
    g() # 22 
    print(X) # 22 - X in function is global
    h1() # 33 - X in h1 is local
    h2() # 44 - X is nonlocal and seen from h2() function
