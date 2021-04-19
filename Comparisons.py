# Chain
x = 10
y = 15
print(x > y and y > z)

# Comparison by 'is' vs '=='
a = 'python is fun!'
b = 'python is fun!'
d = 'e'
print(a == b)
print(a is b)

a = [1, 2, 3, 4, 5]
b = a
print(b)
print(a == b)
print(a is b)
b = a[:]
a == b
print(a is b)
a = 'short'
b = 'short'
c = 5
d = 5
print(a is b)
print(c is d)

a = 'not so short'
b = 'not so short'
c = 1000
d = 1000
print(a is b)
print(c is d)



sentinel = object()
def myfunction(var=sentinel):
    if var is sentinel:
        # value wanst provied.
        pass
    else:
        # value was provided
        pass

# Greater that or less than.

print(12 > 4)
print(12 < 4)

print("alpha" < "beta")

# Not equal to.
print(12 != 1)
print('12' != '12')

# Equal to.
print(12 == 12)

# Comparison object.
a = Foo(5)
b = Foo(5)
print(a == b)
print(a != b)
class Bar(object):
    def __init__(self, item):
        self.other_item = item
    def __eq__(self, other):
        return self.other_item == other.other_item
    def __ne__ (self, other):
        return self.oter_item != other.other_item
c = Bar(5)
print(a == c)