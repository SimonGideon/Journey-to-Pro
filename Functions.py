def greet():
    print("Hello")

def greet_two(greeting="Howdy"):
    print(greeting)
    greet_two()

def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0
    print(many_types(1))

# Defining a function with arbitirary number of arguments.
def func(*args):
    for i in args:
        print(i)
func(1, 2, 3)

# Arbitirary number of keyword arguments.
def func(**kwargs):
    for name, value in kwargs.items():
        print(name, value)
func()

# Lambda Function.
def greetings():
    return "Hello"
print(greetings())

greet_me = lambda : "Hello"
print(greet_me())

def foo(msg):
    print(msg)
greet = lambda x = "hello world": foo(x)
greet()

# Defining a function with optional arguments.
def make(action='nothimg'):
    return action
make("fun")

# Defining a function with optional mutable arguments.
def f(a, b=42, c=[]):
    pass
print(f.__defaults__)


# Returning a value from a function.
def give_me_five():
    return 5
print(give_me_five())


# Closure.
def makeInc(x):
    def inc(y):
        return y + x
    return inc
incOne = makeInc(1)
incFive = makeInc(5)

incOne(5)
incFive(5)



# Focing the use of named parameters.
def f(*a, b):
    pass
f(1, 2, 3)

# Nested functions.
def fibonacci(n):
    def step(a, b):
        return b, a+b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a
def make_adder(n):
    def adder(x):
        return n + x
    return adder
add5 = make_adder(5)
add6 = make_adder(6)
add5(10)


# Recursion limit.
def cursing(depth):
    try:
        cursing(depth + 1)
    except RuntimeError as RE:
        print('I recursed {} times!'.format(depth))
print(cursing(0))

# Recursive Lambda using assigned variables.
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4))

# Defining a function with an argument.
def divide(dividend, divisor):
    print(dividend / divisor)


# Defining a function with multiple arguments.
def func(value1, value2, optionalvalue=10):
    return '{0} {1} {2}'.format(value1, value2, optionalvalue1)
print(func(1, 'a', 100))

# Defining functions with list arguments.
def func(mylist):
    for item in mylist:
        print(item)

func([1,2,3,4,5,7])


