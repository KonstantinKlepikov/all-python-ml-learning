# example of asser usage

def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


if __name__ == "__main__":
    f(1)

"""
Traceback (most recent call last):
File "assert.py", line 9, in <module>
f(1)
File "assert.py", line 4, in f
assert x < 0, 'x must be negative'
AssertionError: x must be negative
"""

# for usage without assert run:
# python -O assert.py
