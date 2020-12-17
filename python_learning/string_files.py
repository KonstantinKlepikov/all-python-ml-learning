# example of usage text and bytes files

# basics of text files
file = open('content/temp.txt', 'w') # write as text
size = file.write('abc\n')
file.close() # hand-closed file

file = open('content/temp.txt') # standard regime r (rt)
text = file.read()
print(text) # abc

# writing as text, reading as text or bytes
open('content/temp.txt', 'w').write('xyz\n') # write as text
print(open('content/temp.txt', 'r').read()) # xyz read as text
print(open('content/temp.txt', 'rb').read()) # b'xyz\n' read as bytes

# writing as bytes, reading as text or bytes
open('content/temp.txt', 'wb').write(b'xyz\n') # write as bytes
print(open('content/temp.txt', 'r').read()) # xyz read as text
print(open('content/temp.txt', 'rb').read()) # b'xyz\n' read as bytes

# writes as bytes (that regim of writing can operate only with bytes or bytearray data)
ba = bytearray(b'\x01\x02\x03D')
open('content/temp.txt', 'wb').write(ba) # # write as bytes
print(open('content/temp.txt', 'r').read()) # D files read as text
print(open('content/temp.txt', 'rb').read()) # b'\x01\x02\x03' read as bytes

# !!! Important
# we cant write str as bytes file and bytes as str file


# writing and reading unicode data

# hand method
# hand encoding
s = 'A\xc4B\xe8C'
print(s, len(s)) # AÄBèC 5

l = s.encode('latin-1')
print(l, len(l)) # b'A\xc4B\xe8C' 5

u = s.encode('utf-8')
print(u, len(u)) # b'A\xc3\x84B\xc3\xa8C' 7

# encoding with open
open('content/temp.txt', 'w', encoding='latin-1').write(s)
print(open('content/temp.txt', 'rb').read()) # b'A\xc4B\xe8C'

open('content/temp.txt', 'w', encoding='utf-8').write(s)
print(open('content/temp.txt', 'rb').read()) # b'A\xc3\x84B\xc3\xa8C'

# decoding with open
open('content/temp.txt', 'w', encoding='latin-1').write(s)
print(open('content/temp.txt', 'r', encoding='latin-1').read()) # AÄBèC

open('content/temp.txt', 'w', encoding='utf-8').write(s)
print(open('content/temp.txt', 'r', encoding='utf-8').read()) # AÄBèC

# for BOM usage look in book


# names of files and unicode streams



if __name__ == "__main__":
    pass
