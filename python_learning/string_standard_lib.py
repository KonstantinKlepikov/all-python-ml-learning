# some examples of standard library modules, that use str or bytes types


# re
import re

s = 'Bugger all down here on earth!'
u = b'Bugger all down here on earth!'

print(re.match('(.*) down (.*) on (.*)', s).groups()) # ('Bugger all', 'here', 'earth!')
print(re.match(b'(.*) down (.*) on (.*)', u).groups()) # (b'Bugger all', b'here', b'earth!')


# struct
import struct

print(struct.pack('>i4sh', 7, b'spam', 8)) # b'\x00\x00\x00\x07spam\x00\x08'

b = struct.pack('>i4sh', 7, b'spam', 8)
print(b) # b'\x00\x00\x00\x07spam\x00\x08'

v = struct.unpack('>i4sh', b)
print(v) # (7, b'spam', 8)

f = open('content/data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data) # b'\x00\x00\x00\x07spam\x00\x08'
f.write(data)
f.close()

f = open('content/data.bin', 'rb')
data = f.read()
print(data)
v = struct.unpack('>i4sh', data)
print(v) # (7, b'spam', 8)
f.close()

# operations over packed data
print(bin(v[0]), v[0] & 0x01, v[0] | 0b1010, bool(v[0] & 0b1000)) # 0b111 1 15 False
print(v[1], v[1][0], v[1][:1]) # b'spam' 115 b's'


# picke
import pickle

# pickle always use bytes regime for files
pickle.dump([1, 2, 3], open('content/pickdata', 'wb'))
print(pickle.load(open('content/pickdata', 'rb'))) # [1, 2, 3]
print(open('content/pickdata', 'rb').read()) # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'


# XML look at book