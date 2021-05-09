# Combination metod in ittertools Module.
import itertools
a = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2 == 0

lst = [0, 2, 3, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))
print(result)

# Zipping two iterators until they are both exhausted.
from itertools import zip_longest
a = [i for i in range(5)]
b = ['a','b','c','d','e','f','g']
for i in zip_longest(a, b):
    x,y = i
    print(x, y)

# Take a slice of a generator.
import itertools
def gen():
    n = 0
    while n < 20:
        n += 1
        yield n
for part in itertools.islice(gen(), 3):
    print(part)



# Itertools.take while.
def is_even(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.takewhile(is_even, lst))
print(result)

# Ittertools.permutations.
a = [1, 2, 3]
print(list(itertools.permutations(a)))

# Itertools.repeat.
import itertools
for i in itertools.repeat('over and over', 3):
    print(i)

    # GEt an accuulated sum of numbers in an iterable.
import itertools as it
import operator
print(list(it.accumulate([1, 2, 3, 4, 5])))

# Cycle through elements in an iterator.
import itertools as it
print(it.cycle('ABSD'))

# itertools.product
from itertools import product
a=[1, 2, 3, 4, 5]
b=['a','b', 'c']
print(product(a,b))

# itertools.count
for number in itertools.count():
    if number > 20:
        break
    print(number)


# Chaining mutiple iterators together.
from itertools import chain
a = (x, for x in ['1', '2', '3', '4'])
b = (x for x in ['x', 'y', 'z'])
print(''.join(chain(a, b)))


