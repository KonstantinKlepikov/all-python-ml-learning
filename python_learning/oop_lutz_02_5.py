# example of nested class part 1

X = 1

def nester1():
    print(X) # global X

    class C:
        print(X) # global X

        def method1(self):
            print(X) # global X

        def method2(self):
            X = 3
            print(X) # local X

    I = C()
    I.method1()
    I.method2()

print(X) # 1
nester1() # 1, 1, 1, 3
print('_'*40)

def nester2():
    X = 2 # hide global X
    print(X) # local X

    class C:
        print(X) # local X from nested2

        def method1(self):
            print(X) # local X from nested2

        def method2(self):
            X = 3
            print(X) # local X

    I = C()
    I.method1()
    I.method2()

print(X) # 1
nester2() # 2, 2, 2, 3
print('_'*40)

def nester3():
    X = 2 # hide global X
    print(X) # local X of nester3

    class C:
        X = 3 # local X from C.X or I.X (from class or exemplar)
        print(X) # local X from C

        def method1(self):
            print(X) # local X from nested3
            print(self.X) # local X from class C

        def method2(self):
            X = 4 # local X, hide local X from Nester3, but not from class C
            print(X) # local X from method2
            self.X = 5 # hide local X from class C
            print(self.X) # local X from exemplar

    I = C()
    I.method1()
    I.method2()

print(X) # 1
nester3() # 2, 3, 2, 3, 4, 5
print('_'*40)

"""If you want recieve names form class (for ex. methods)
you must call it as attributes of class or exemplar as self.X

Simple names never findes in included classes, only in defs,
modules and in visibility area
"""