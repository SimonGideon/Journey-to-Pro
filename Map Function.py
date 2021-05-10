# Basic use of map, itertools.imap and ufture_builtins.map.
names = ['Fed', 'Wilima', 'Barney']
print(len(item) for item in names)

# Mapping each value in an iterable.
list(map(abs, (1, -1, 2, -2, 3, -3)))
print(map(lambda x: x * 2, [1, 2, 3, 4, 5]))

from functools import partial
from operator import mul

rate = 0.9
dollar = {'under_my_bed': 1000,
          'jeans': 45,
          'bank': 5000}
print(sum(map(partial(mul, rate), dollar.values())))

# Series and Parallel Mapping
insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x: x + 'is an insect'
print(list(map(f, insects)))

# Exponentiation
# Exponentiation Using builtins: ** and pow()
import operator

operator.pow(4, 2)
operator.__pow__(4, 3)
# Square root:
import math

n = math.sqrt(9)
p = math.sqrt(11.11)
print(n, p)


def modular_inverse(x, p):
    """Find a such as ax == 1 (mod p), assuming p is prime."""
    return pow(x, p - 2, p)


print([modular_inverse(x, 13) for x in range(1, 13)])

# Computing large integer roots.
x = 2 ** 100
cube = x ** 3
roo = cube ** (1.0 / 3)


def nth_root(x, n):
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            return mid
    return mid + 1


x = 2 ** 100
cube = x ** 3
root = nth_root(cube, 3)
print(x == root)

# Exponential function: math.exp() and cmath.exp()
import math

math.e ** 2
math.exp(2)
import cmath

cmath.e ** 2
cmath.exp(2)

# Exponential function minus 1:
import math

print(math.e ** 1e-3 - 1)


# Magic methods and exponentiation
class Integer(object):
    def __init__(self, value):
        self.value = int(value)

        def __repr__(self):
            return '{cls}({val})'.format(cls=self.__class__.name__,
                                         val=self.value)

        def __pow__(self, other, modulo=None):
            if modulo is None:
                print('Sing__pow__')
                return self.__class__(self.value ** other)
            else:
                print('Using __pow__ with modulo')
                return self.__class__(pow(self.value, other, modulo))

            def __float__(self):
                print('USing __float__')
                return float(self.value)

            def __complex__(self):
                print('Using __complex__')
                return complex(self.value, 0)


# Sorting, Minimum and Maximum.
class IntegerContainer(object):
    def __init__(self, value):
        self.value = value


def __repr__(self):
    return "{}({})".format(self.__class__.__name__, self.value)


def __lt__(self, other):
    print('{!r} - Test less than {!r}'.format(self, other))
    return self.value < other.value


def __le__(self, other):
    print('{!r} - Test less than or equal to {!r}'.format(self, other))
    return self.value <= other.value


def __gt__(self, other):
    print('{!r} - Test greater than {!r}'.format(self, other))
    return self.value > other.value


def __ge__(self, other):
    print('{!r} - Test greater than or equal to {!r}'.format(self, other))
    return self.value >= other.value


def __eq__(self, other):
    print('{!r} - Test equal to {!r}'.format(self, other))
    return self.value == other.value


def __ne__(self, other):
    print('{!r} - Test not equal to {!r}'.format(self, other))
    return self.value != other.value
# Special case: dictionaries.
adict = {'a': 3, 'b': 5, 'c': 1}
print(min(adict))
print(max(adict))
print(sorted(adict))

print(min(adict.items()))
print(max(adict.items()))

# Using the key argument.
list_of_tuples = [(0, 10), (1, 15), (2, 8)]
print(min(list_of_tuples))

print(min(list_of_tuples, key=lambda x: x[0]))
print(sorted(list_of_tuples, key=lambda x: x[1]))

import operator
print(max(list_of_tuples, key=operator.itemgetter(0)))

# Extracting N largest or N smallest items from an iterable.
import heapq
print(heapq.nlargest(5, range(10)))
print(heapq.nsmallest(5, range(10)))


class MyClass(object):
    def __init__(self, value, name):
        self.value = value
        self.name = name
def __lt__(self, other):
    return self.value < other.value
def __repr__(self):
    return str(self.name)
    sorted([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')])
# Output: [second, first, third]
max([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')])
# Output: first