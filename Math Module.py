# Rounding: round, floor, ceil, trunc
x = 1.55
y = -1.55
print(x)
print(round(y))
print(round(x, 1))
print(round(y, 1))

import math

print(math.floor(x))  # To gt the largest integer less than X

print(math.ceil(x))  # To greater the smallest integer greater than x

# Droping fractional part of X.

print(math.trunc(x))

# Trigonometry.
print(math.hypot(2, 4))

# Converting degrees into a radian.
print(math.radians(45))

# Convert the result of a sin to degrees.
print(math.degrees(math.asin(1)))

# Hyperbolic isne, cosine and tangent
print(math.sinh(math.pi))  # Hyperbolic of sin function

print(math.cosh(math.pi))  # Hyperbolic cosine function.

# Pow for faster exponentiation
from math import pow

print(pow(5, 5))

# Infinity and NaN("not a number")
pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan
print(pos_inf, neg_inf, not_a_num)

print(math.isfinite(0.0))

import sys

print(sys.float_info.max)

# Logarithms.
print(math.log(math.e))

print(math.log(1 + 1e-20))

print(math.log(100, 10))

# Constants.
from math import pi, e

print(pi)
print(e)
print(math.inf == float('inf'))

# Imaginary Numbers.
"""Imaginary numbers are represented as 'j' and 'J'"""

# Copying Signs.
print(math.copysign(-2, 3))
print(math.copysign(1, -0.0))

# Complex numbers and the cmath module.
z = 1 + 3j
print(z.real, z.imag)
print(z.conjugate())

# Complex Math
import cmath

z = 2 + 3j
print(cmath.phase(z))
print(cmath.polar(z))
print(cmath.rect(2, cmath.pi / 2))

# Square root.
print(cmath.sqrt(z))

# Trigonometric functions.
print(cmath.sin(z))
print(cmath.asin(z))
print(cmath.sin(z) ** 2 + cmath.cos(z) ** 2)

# Basic complex arithmetic.
z = 2 + 3j
w = 1 - 7j
print(z + w)
print(z - w)
print(z * w)
print(z / w)

# Collections Module.
# Collection Counter
import collections
counts = collections.Counter([1, 2, 3])
print(counts)
print(collections.Counter('Happy Birthday'))


# Collection OrderedDict
d = {'foo': 5, 'bar': 6}
print(d)
d['baz'] = 7
print(d)

from collections import OrderedDict
d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)


# Collections.namedtuple.
from collections import namedtuple
Person = namedtuple('Person', ['age', 'height', 'name'])
Person = namedtuple('Person', 'age, height, name')
dave = Person(30, 178, 'Dave')
print(dave.age)

# Collection.deque
from collections import deque
d = deque('ghi') # make a new deque with three items
for elem in d:
    print(elem.upper())

# Collections.ChainMap.
import collections
# define two dictionaries with at least some keys overlapping.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}
combined_dict = collections.ChainMap(dict1, dict2)
reverse_ordered_dict = collections.ChainMap(dict2, dict1)

for k, v in combined_dict.items():
    print(k, v)
# Operator Modules.
# Itemgetter.
from itertools import groupby
from operator import itemgetter
adict = {'a': 1, 'b': 5, 'c': 1}
print(dict((i, dict(v)) for i, v in groupby(adict.items(), itemgetter(1))))

# Operators as alternatives to fix operator.
from operator import  add
print(add(1, 10))

from operator import mul
print(mul(1, 49))

# Methodcaller.
from operator import methodcaller
print(list(filter(methodcaller('startswith', 'd'), alist)))