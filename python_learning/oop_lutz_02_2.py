# example of definitions of names part 1

#global name or attribute of module (X or oop_lutz_02_2.X)
X = 11

# access to global name from function
def f():
    print(X)

# local variable in function (X, hides moduls X)
def g():
    X = 22
    print(X)

class C:
    X = 33 # class attribute (C.X)
    def m(self):
        X = 44 # local variable in method (X)
        self.X = 55 # attr of exemplar (exemplar.X)


if __name__ == '__main__':
    print(X) # 11
    f() # 11
    g() # 22
    print(X) # 11
    ex = C()
    print(ex.X) # 33
    ex.m() # add attr X to exemplar
    print(ex.X) # 55
    print(C.X) # 33
    # print(C.m.X) # err - only from method
    #print(g.X) # err - only from function
