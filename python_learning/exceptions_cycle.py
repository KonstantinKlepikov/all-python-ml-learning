# example of usage exceptions as break point

class Exitloop(Exception):
    pass


try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise Exception
                    print('loop3: {}'.format(i))
            print('loop2')
        print('loop1')
except Exception:
    print(i) # 4

"""
# this provoke infinite cycle, because breake cant exit from outer cycles
while True:
    while True:
        for i in range(10):
            if i > 3:
                breake
            print('loop3: {}'.format(i))
        print('loop2')
    print('loop1')
print(i) # 4
"""
