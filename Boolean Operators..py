def or_(a, b):
    if a:
        return a
    else:
        return b


"""Will return the first value in the expression if  it's true,
second value"""


def and_(a, b):
    if not a:
        return a
    else:
        return b


"""It will return first value if its false,
last value"""



if 3.14 < 3.142:
    print("X is near pi")

# Short-circuit evaluation.
def true_func():
    print("true_func()")
    return True
def false_func():
    print("false_function()")
    print(False)
true_func() or false_func()
true_func()
True
false_func() or true_func()
false_func()
true_func()
True
true_func()
false_func()
False
false_func() and false_func()
false_func()
False

# and.
x = True
y = True
z = x and y
print(z)

x = True
y = False
z = x and y
print(z)

x = True
y = False
z = x and y
print(z)

x = 1
y = 1
z = x and y
print(z)
# 'and' and  'or' are not guranteed in a boolean.

x = 0
y = 1
z = x and y
print(z)
x = 1
y = 0
z = x and y
print(z)

x = 0
y = 0
z = x and y
print(z)

# or.
x = True
y = True
z = x or y
print(z)

x = True
y = False
z = x and y

x = False
y = True
z = x or y
print(z)

x = False
y = False
z = x or y
print(z)

# not.
x = True
y = not x

"""not return the opposite value"""
x = False
y = not x
print(y)