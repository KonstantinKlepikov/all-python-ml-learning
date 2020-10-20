# example of else usage in exception cauting

def kaboom(x, y):
    print(x + y)

try:
    kaboom([0, 1, 2], 'spam')
except TypeError:
    print('Hello world')
else:
    print('Not here')
print('Resume here')
