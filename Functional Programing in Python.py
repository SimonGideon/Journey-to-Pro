# LAmbda function.
s=lambda  x:x*x
# Map function.
name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(name_lengths)


# Reduce function.
""""
total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)"""

# Filter function.
arr=[1, 2, 3, 4, 5, 6]
[i for i in filter(lambda x:x>4,arr)]


# Partial functions.

def raise_power(x, y):
    if y in (3, 4, 5):
        return x**y
    raise NumberNotInRangeException("You should provide a valid exponent")

# Decorators.
def super_secrete_function(f):
    return f
@super_secrete_function
def my_function():
    print("This is my secrete function")
def disable(f):
    """THis function returns nothing,  and hence the decorated function
    from the local scope"""
pass
@disable
def my_function():
    print("THis function can nolonger be called....")
# This is the decorator
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) # Call the original function with its arguments.
    return inner_func
@print_args
def multiply(num_a, num_b):
    return num_a * num_b
print(multiply(3, 5))


# Decorator Class.
class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res
@Decorator
def testfunc():
    print('Inside the function.')
testfunc()

# Decorator with arguments(decorator factory)
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator
@decoratorfactory('Hello World')
def test():
    pass

test()


# Decorator classes
def decoratorfactory(*decorator_args, **decorator_kwargs):

    class Decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(decorator_args))
            return self.func(*args, **kwargs)
    return Decorator
@decoratorfactory(10)
def test():
    pass
test()

# Making a decorator look like the decorated function.
from functools import wraps
def decorator(func):
    # Copies the docstring, name, annotations and module to the decorator
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped_func
@decorator
def test():
    """Doc string test"""
    pass
test.__name__

# Using a decorator to time a function.
import time
def time(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Runtime took {0} seconds'.format(t2-t1))
        return f
    return inner
@time
def example_function():
    example_function()

# Create singleton class with a decorator.
def singleton(cls):
    isinstance = [None]
    def wrapper(*args, **kwargs):
        if isinstance[0] is None:
            isinstance[0] = cls(*args, **kwargs)
        return isinstance[0]
    return wrapper
@singleton
class SomeSingletonClass:
    x = 2
    def __init__(self):
        print("Created!")
isinstance = SomeSingletonClass()
isinstance = SomeSingletonClass()
print(input(isinstance.x))

isinstance.x = 3
print(SomeSingletonClass().x)