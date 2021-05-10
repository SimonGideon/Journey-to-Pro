from functools import reduce


def add(s1, s2):
    return s1 + s2


asequence = [1, 2, 3]
reduce(add, asequence)

import operator

reduce(operator.add, asequence)

reduce(add, asequence, 10)

# Using reduce.
"""def multiply(s1, s2):
    print('{arg1} * {arg2} = {res}'.format(arg1,
                                           arg2,
                                           res=s1*s2))
    return s1 * s2
asequence = [1, 2, 3]"""
import operator

cumprod = reduce(multiply, asequence, 5)
print(cumprod)
