# base examples of string tapes

# string literals

b = b'spam'
s = 'eggs'
print(type(b), type(s)) # <class 'bytes'> <class 'str'>
print(b, s) # b'spam' eggs
print(b[0], s[0]) # 115 e
print(b[1], s[1]) # 112 g
print(b[1:], s[1:]) # b'pam' ggs
print(list(b), list(s)) # [115, 112, 97, 109] ['e', 'g', 'g', 's']
b = b"""
xxx
zzz
AAA
"""
print(b) # b'\nxxx\nzzz\nAAA\n'

# old version of unicode literals is available for back compatibility

u = u'spam'
print(type(u), u, u[0], list(u)) # <class 'str'> spam s ['s', 'p', 'a', 'm']

# in python 3.x str and bytes neer be mixed 
# and never be translated automaticaly

s = 'eggs'
print(s.encode()) # code to bytes
print(bytes(s, encoding='ascii')) # alternative method
b = b'spam'
print(b.decode()) # decode to str
print(str(b, encoding='ascii')) # alternative method

import sys, locale

# encoding argument for bytes() is required
# encoding argument in str.encode() vytes.decode() isnt require
# if encodng argument isnt used in str(), 
# that method return sting, even is ita byte sring
print(sys.platform, sys.getdefaultencoding(), locale.getpreferredencoding(False))
b = b'spam'
print(str(b)) # b'spam'
print(str(b, encoding='utf-8')) # spam
print(len(str(b)), len(str(b, encoding='utf-8'))) # 7 4

# writing unicode strings

# ASCII text

print(ord('X')) # 88
print(chr(88)) #'X

s = 'XYZ'
print(len(s)) # 3
print([ord(c) for c in s]) # [88, 89, 90]

print(s.encode('ascii')) # b'XYZ'
print(s.encode('latin-1')) # b'XYZ'
print(s.encode('utf-8')) # b'XYZ'

print(s.encode('latin-1')) # b'XYZ'
print(s.encode('latin-1')[0]) # 88
print(list(s.encode('latin-1'))) # [88, 89, 90]

# non ASCII text

s = '\u00c4\u00e8'
print(s)
# print(s.encode('ascii')) UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
print(s.encode('latin-1'), len(s.encode('latin-1'))) # b'\xc4\xe8' 2
print(s.encode('utf-8'), len(s.encode('utf-8'))) # b'\xc3\x84\xc3\xa8' 4

# for other types of coding/decoding look in book