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

# bytes literals

# str can detect 16-th and unicode
s = 'A\xC4B\xE8C'
su = 'A\u00C4B\U000000E8C'
print(s, su) # AÄBèC AÄBèC

# bytes can detect 16-th, but cant unicode
b = b'A\xC4B\xE8C'
bu = b'A\u00C4B\U000000E8C'
print(b, bu) # b'A\xc4B\xe8C' b'A\\u00C4B\\U000000E8C'

# transformation between encodings

b = b'A\xc3\x84B\xc3\xa8C' # utf-8
s = b.decode('utf-8') # unicode in utf-8
print(s) # AÄBèC
t = s.encode('cp500') # bytes in EBCDIC
print(t) # b'\xc1c\xc2T\xc3'
u = t.decode('cp500') # unicode with EBCDIC
print(u) # AÄBèC
print(u.encode()) # b'A\xc3\x84B\xc3\xa8C' bytes with utf-8

# bytes objects and bytes attributes

# attributes
print(set(dir('abc')) - set(dir(b'abc')))
# {'format_map', 'casefold', 'encode', 'isprintable', 'isdecimal', 'isidentifier', 'format', 'isnumeric'}

print(set(dir(b'abc')) - set(dir('abc')))
# {'decode', 'hex', 'fromhex'}

# other methods for bytes generation

b = b'abc' # literal
b = bytes('abc', 'ascii') # constructor with encoding definition
b = bytes([97, 98, 99]) # iterated object with whole numbers
b = 'spam'.encode() # str.encode()

# bytearray

s = 'spam'
c = bytearray(s, 'utf-8')
print(c) # bytearray(b'spam')
b = b'spam'
c = bytearray(b)
print(c) # bytearray(b'spam')

print(c[0])
c[0] = ord('x') # we can use only ordinal value 0-255 ASCII
print(c) # bytearray(b'xpam')

# attributes
print(set(dir('abc')) - set(dir(bytearray(b'abc'))))
# {'casefold', 'format_map', 'isprintable', 'isnumeric', 'isdecimal', 'format', '__getnewargs__', 'encode', 'isidentifier'}

print(set(dir(bytearray(b'abc'))) - set(dir('abc')))
# {'append', '__iadd__', 'fromhex', 'extend', 'reverse', '__setitem__', '__delitem__', '__imul__', 'hex', '__alloc__', 'clear', 'remove', 'decode', 'insert', 'copy', 'pop'}

c.append(ord('L'))
print(c) # bytearray(b'xpamL')
c.extend(b'MNO')
print(c) # bytearray(b'xpamLMNO')
# and etc...
