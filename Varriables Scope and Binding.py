# Nonlocal Variables.
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()
print(c())
"""'nonlocal' allows assign vrriables in an outer scope
not global scope"""

# Global Variables.
x = 'Hi'
def read_x():
    print(x) # x is just referenced, therefore assumed global.
read_x()


def read_y():
    print(y) # This is just a refrenced therefore assumeb global.
def read_y():
    y = 'Hey' # y appears as an assignmet, local.
    print(y)
read_y()

x = 'Hi'
def change_local_x():
    x = 'Bye'
    print(x)
change_local_x()
print(x)

x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x()
print(x)
x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x()
print(x)

# Local Variables.
def foo():
    if True:
        a = 5
    print(a)

# The del command.
class A:
    pass

a = A()
a.x = 7
print(a.x)
"""del a.x
print(a.x)
del v[item]"""

x = [0, 1, 2, 3, 4]
del x[1:3] # Deltes the characters in the range "1-3"
print(x)

# Function skip class scope when looking up names.
a = 'global'

class Fred:
    a = 'class' # class scope
    b = (a for i in range(10)) # Function scope
    c = [a for i in range(10)] # Function scope.
    d = a # Class scope
    e = lambda: a # function scope
    f = lambda a=a: a # default argument uses class scope.
    @staticmethod # or @classmethod, or regular instance ,method
    def g(): # function scope
        return a
print(Fred.a)
print(next(Fred.b))
print(Fred.c[0])
print(Fred.d)
print(Fred.e())
print(Fred.f())
print(Fred.g()

# Functions within functions.
def f1():

    def f2():
        foo = 2 # a new foo local in f2

        def f3():
            nonlocal foo # fooo from f2, which is the nearest enclosing scope.
            print(foo)
            foo = 20 # Modifies foo from f2!
