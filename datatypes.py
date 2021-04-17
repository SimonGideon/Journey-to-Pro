# Built-in types
# Booleans
# Boolean can either be true oo false.

issubclass(bool, int)
print(True + False == 1)  # 1 + 0 == 1; True == 1 and False == 0.
print(True * True == 0)  # 1 * 1 == 1 not 0; False.

# Numbers.
b = 100.e1  # floating
print(b)
a = 2 + 1j
b = 100 + 10J
print((a + b))  # Complex numbers.

# Strings
a = reversed('hello')
print(a)
i = 7
if isinstance(i, int):
    print(i + 1)
elif isinstance(i, str):
    i = int(i)
    print(i + 1)
# instance is used to test the data type for conditionla statement.
x = None
if x is None:  # To test None data type
    print('I just defined x a none')
a = '123'
b = int(a)  # converting data type from string to integer.
print(b)

a = '123.456'
b = float(a)
d = int(b)
print(a, b, d)
# converting sequences or collection types.
a = 'sevens'
b = list(a)
x = set(a)
d = tuple(a)
MyList = [b, x, d]
for I in MyList:
    print(I)


# Mutable and immutable data types.
def f(m):
    m.append(3)  # adds a number to the list. This is mutation.


x = [1, 2]
f(x)
x == [1, 2]  # False now, since an item was added to the list.
a_str = 'This is what we do'
print(a_str)
print(a_str[0])
print(a_str[0:5])

# Set Data Type
basket = {'apple', 'mango', 'pear' 'pear', 'banana'}  # Duplicate will be removed.
print(basket)
a = set('abracadabra')  # set represents only once for repeated characters.
print(a)
a.add('s')
print(a)

# sets are mutable.
b = frozenset('abcdefghijkl')
print(b)
cities = frozenset(["Frankfruit", "Basel", "Freiburg"])
print(cities)
# Frozen Sets is immutable.

# Numbers Data type.
a = int_num = 10  # integer value
float_num = 10.2  # float value.
complex_num = 3.142j  # Complex value
long_num = 1235789  # Long value

# Dictionary DAta type
dic = {'name': 'red', 'age': 10}
print(dic)
print(dic['name'])  # Outputs value with 'name' key.
print(dic.values())  # Output list of value in dic.
print(dic.keys())  # Output list of keys

# Tuple data type.
# Tuples are immutable.
tuple = (123, 'hello', 'me')
tuple1 = ('world')
print(tuple)
print(tuple[2])



