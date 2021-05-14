def switch(value):
    if value == 1:
        return "one"
    if value == 2:
        return "Two"
    if value == 42:
        return " The answer to the question about life, the universe and everything"
    raise Exception("No case found!")
print(switch(1))
print(switch(2))
print(switch(1))

# Use a dict of function.
switch = {
    1: lambda: 'one',
    2: lambda: 'two',
    42: lambda: 'the answer of life the universe and everything',
}
def default_case():
    raise Exception('No case found!')
print(switch.get(42, default_case)())


# LIst destruction.
head, *tail = [1, 2, 3, 4, 5]
print(head)
def fun1(*args, **kwargs):
    print(args, kwargs)

# Accessing python source code and bytecode.
import  random
import inspect
print(inspect.getsource(random.randint))

def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)
dir(fib.__code__)
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)
dir(fib.__code__)


# Mixin
class Vehicle(object):
    """A generic vehicle class."""
    def __init__(self, position):
        self.position = position
    def travel(self, destination):
        route = calculate_route(from=self.position, to=destination)
        self.move_along(route)
class Car(Vehicle):
    ...
class Boat(Vehicle):
    ...
class Plane(Vehicle):
    ...

class Mixin1(object):
    def test(self):
        print("Mixin1")
class Mixin2(object):
    def test(self):
        print("Mixin2")
class BaseClass(object):
    def test(self):
        print("Base")
class MyClass(BaseClass, Mixin1, Mixin2):
    pass


