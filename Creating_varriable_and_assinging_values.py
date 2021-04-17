# Integer
a = 2
print(a)
b = 9233345555556556
print(b)

# Floating point
pi = 3.14
print(pi)

# Strings
c = 'A'
print(c)
name = 'Simon Gideon'
print(name)
# Boolean
q = True
print(q)
# EMpty value for null data type
x = None
print(x)

# varriable assingment works from left to right.

print(type(x))

print(type(q))
print(type(c))
print(type(a))
print(type(b))
print(type(name))
print(type(pi))
# Py automatically  picks the most suitable buillt-in type for it.


"""a, b, c = 1, 2, 3
print(a, b, c)"""  # name should have the same variable.

a, b, _ = 1, 2, 3  # _ is used to remove unwanted value.
print(a, b, )
# The number of _ should be equal to the number of unwanted values.
a, b, _, _ = 91, 52, 53, 48
print(a, b)

# A single variable can be assinged to svral values.
a = b = c = 1
print(a, b, c)  # all three names a, b and c refer to same int object with value 1.

b = 5  # varriable 'b' is now refering to another object 5.

print(a, b, c)

x = y = [7, 8, 9]
x[0] = 13  # The value at the first osition of the object is replaced with 13.
print(y)
# FOr nested list
x = [1, 2, [3, 4, 5], 6, 7]
print(x[2])
print(x[2][1])
a = 7
print(a)

a = 'I love coding'
print(a) # varriable can be changed from what was assigned at first.


