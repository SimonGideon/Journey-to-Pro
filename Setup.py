# Reucrsions.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib(n - 1)
        return (a + b, a)


root = get_root(tree)
for node in get_children(root):
    print(get_name(node))
    for child in get_children(node):
        print(get_name(child))
        for grand_child in get_children(child):
            print(get_name(grand_child))

# Sum of numbers fromm 1 to n
n = 0
for i in range(1, n + 1):
    n += i


# Tail Recursion - Bad Practice.
def countdown(n):
    if n == 0:
        print(n)
        countdown(n - 1)


def find_max(seq, max_so_far):
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:
        return find_max(seq[1:], seq[0])
    else:
        return find_max(seq[1:], max_so_far)


# Adding command line scrips to your python package
from setuptools import setup

setup(
    name='greetings',
    scripts=['hello_world.py']
)


@tail_call_optimized
def fib(i, current=0, next=1):
    if i == -0:
        return current
    else:
        return fib(i - 1, next, current + next)


print(fib(10000))

# Type Hints.
def two_sum(a, b):


    return a  + b
print(two_sum(2, 1))


# Name Tuple.
import typing
Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
# Class Member and Methods.
class A:
    x = None
    def __init__(self, X: float): -> None:
    """
    self should not be annotated
    init should be annoted to return None
    """
    self.x = x
@classmethod
def from_int(cls, x: int) -> 'A':
    """
    cls should not be annoted
    Use forwatd refernce to refer to curent class with string literal 'A'

    """
    return
cls(float(x))