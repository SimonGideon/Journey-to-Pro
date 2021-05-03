class Person(object):
    """A simple class"""
    speciies = "Homo Sapiens" # Class Attribute

    def __init__(self, name):    # Specila method
        """This is the initialzer. It is
        a special method """
        self.name = name
    def __str__(self):
        """Thismethod is run when Python tries to cast the object to a string.
        Return this string when using print()"""
        return self.name
    def rename(self, rename):
        """Reassign and print the name attribute"""
        self.name = rename

        print("Now my name is {}".format(self.name))

# Bound, unbound, and static method.
class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x
    @staticmethod
    def g(name):
        print("Hello, %s" % name)
s = D.f(12)
n = D.g
p = D.g("World")
for i in [s, n, p]:
    print(i)
d = D()
d.multiplier = 1337
print(D.multiplier, d.multiplier)

# Basic inheritance.
class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w* self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
class Square(Rectangle):
    def __init__(self, s):
        # Call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s
# Instantiate.
r = Rectangle(3, 4)
s = Square(2)
a = isinstance(r, Rectangle)
b = isinstance(r, Square)
c = isinstance(s, Rectangle)
d = isinstance(s, Square)
for i in [a, b, c, d]:
    print(i)
# MOnkey Patching.
class A(object):
    def __int__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)

# Class method: alternate initializers
class Person(object):
    def __init__(self, firts_name, last_name, age):
        self.first_name = firts_name
        self.last_name = last_name
        self.age = age
        self.full_name = firts_name + "" + last_name
@classmethod
def from_full_name(cls, name, age):
    if "" not in name:
        raise ValueError
    first_name, last_name = name.split(" ",2)
    return cls(first_name, last_name, age)
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")
bob = Person("Bob", "Bobberson", 42)
alice = Person("Alice", "Henderson", 31)


# Multiple Inheritance.
