# example of definitions of names part 2

import oop_lutz_02_2

X = 66
print(X) # 66
print(oop_lutz_02_2.X) # 11 attribute of module

oop_lutz_02_2.f() # 11
oop_lutz_02_2.g() # 22

print(oop_lutz_02_2.C.X) # 33 attr of class as attr of module
I = oop_lutz_02_2.C() # exemplr of class from module
print(I.X) # 33
I.m() # add attr X to exemplar
print(I.X) # 55
