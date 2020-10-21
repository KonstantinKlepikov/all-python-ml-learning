# example of unificated try (python 3.X)

sep = '-' * 45 + '\n'

print(sep + 'Eexception raised and caught')

try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'No exception raised')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'No exception raised with else')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(sep + 'Eexception raised but not caught')
try:
    x = 1 / 0
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')
