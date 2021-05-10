# PyDotPlus.

pip install pydotplus

import pydotplus
graph_a = pydotplus.graph_from_dot_file('demo.dot')
graph_a.write_svg('test.svg')



# PyGraphviz
pip install pygraphviz
G = pgv.AGraph("demo.dot")
G.draw('test', format='svg', prog='dot')

# Generators.
sum(i for i in range(10) if i % 2 == 0)
any(x = 0 for x in foo)
type(a>b for a in foo if a % 2 == 1)

for x in g1:
    print("Received", x)


# Infinite sequences.
import itertools
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
first_ten_fibs = list(itertools.islice(fibonacci(), 10))

def nth_fib(n):
    return next(itertools.islice(fibonacci(), n -1, n))
# Sending objects to a generator.
def accumulator():
    total = 0
    value = None
    while True:
        value = yield total
        if value is None: break
        total += value
generator = accumulator()
next(generator)

generator.send(1)
generator.send(10)
generator.send(100)

# Yielding all value from another iterable
def foob(x):
    yield from range(x*2)
    yield from range(2)
list(foob(5))


def fibto(n):
    a, b = 1, 1
    while True:
        if a >=n: break
        yield a
        a, b = b, a + b
def usefib():
    yield from fibto(10)
    yield from fibto(20)
list(usefib())


# Iteration.
def xrange(n):
    i = 0
    while 1 < n:
        i += 1
for i in xrange(10):
    print(i)

def nums():
    yield 1
    yield 2
    yield 3
generator = nums()
next(generator, None)
next(generator,  None)
next(generator, None)

# Coroutines.
def coroutine(func):
    def start(*args, **kwargs)
        next(cr)
        return cr
    return start
@coroutine
def adder(sum = 0):
    while True:
        x = yield sum
        sum += x
s = adder()
s.send(1)

# Refactoring list-building code
def create():
    result = []
    result.append(value)
    return result
def create_gen():
    yield value
    return
value = list(create_gen())

# Generator expression.
def fib(a=0, b=1):
    """Generator that yields Fibonacci numbers. 'a' and 'b' are the seed value"""
    while True:
        yield a
        a, b = b, a + b
f = fib()
print(','.join(str(next(f)) for _ in range(10)))
# Iterating over generators in parallel.
for x, y in zip(a,b):
    print(x, y)
    

