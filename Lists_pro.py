import itertools

a = [1, 2, 3, 4, 5]
a.append(6)
a.append(7)
b = [8, 9, 10]
a.append(b)
my_string = "hello world"
a.append(my_string)
print(a)

# Extend lists.
a = [1, 2, 3, 4, 5, 6, 7]
b = [8, 9, 10]
a.extend(b)
a.extend(range(3))
a = [1, 2, 3, 4, 5, 6] + [7, 8] + b
a.reverse()
a.sort()
a.sort(reverse=True)
print(a)

import datetime


class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


a = [Person("John Mark", datetime.date(1992, 9, 12), 175),
     Person("Victor Wong", datetime.date(1990, 8, 28), 180),
     Person("John Skeet", datetime.date(1991, 7, 6), 185)]
a.sort(key=lambda item: item.name)
a.sort(key=lambda item: item.birthday)
a.sort(key=lambda item: item.height)
print(a)
# Way to sort using attrgetter and itemgetter.
from operator import itemgetter, attrgetter

people = [{'name': 'chandan', 'age': 20, 'salary': 2000},
          {'name': 'chetan', 'age': 18, 'salary': 5000},
          {'name': 'guru', 'age': 30, 'salary': 3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)
people.sort(key=by_salary)

list_of_tuples = [(1, 2), (3, 4), (5, 0)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples)

a = list(range(10))

for i in a:
    print(i)

del a[::2]
del a[-1]

print(a)
aa = a.copy()
print(aa)

# Accessing list Values.
lst = [1, 2, 3, 4]
print(lst[0])
print(lst[1:])

# Advance Slicing.
data = 'chandan purohit 22 200'
name_slice = slice(0, 19)
age_slice = slice(19, 21)
salary_slice = slice(22, None)

print(data[name_slice])
print(data[age_slice])
print(data[salary_slice])
lst = []
if not lst:
    print("list is empty")

# Iterating Over List.
my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)
for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))

"""Iterating based on the index value"""
for i in range(0, len(my_list)):
    print(my_list)

"""Checking wheitheer an item is the list"""
list = ['test', 'twest', 'tweast', 'treast']
print('test' in list)

# Any and All.
nums = [1, 1, 0, 1]
print(all(nums))
print(any(nums))

# Reversing list elements.

for i in range(0, 10):
    print(i, end=" ")

    break
numbers = [1, 2, 3, 4, 5, 6]
numbers[::-1]
print(numbers)

# Concatenation and Merging Lists.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

alist = []
"""print(len(list(zip(alist, blist))))"""
alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)

# Length of list.
print(len(['one', 'two']))
print(len(['one', [2, 3], 'four']))

# Removing Duplicate Values.
"""list():
name = ["Luke", "Jose", "Edith", "Luke"]
list(set(name))"""

# Comparison of list
n = [1, 10, 100] < [2, 10, 100]

print(n)
p = [1, 10] < [1, 10, 100]
print(p)

# Accessing Values in nested list.
alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
print(alist[0][0][1])  # Accessing the second element in the first list in the first list.
print(alist[1][1][2])  # Accesing the third elemnt in the second list in the secondlist.

# Performing support operations.
alist[0][0].append(1)
print(alist[0][0][2])

# Nested for loops.
for row in alist:  # One way loop through nested list.
    for col in row:
        print(col)
for row in range(len(alist)):
    for col in range(len(alist[row])):
        print(alist[row][col])
# Using slicing.
print(alist[1][1:])
print(alist)

# Initializing a list to a fixed number.
my_list = [None] * 10
my_list = ['test'] * 10

my_list.append('Name')
print(my_list)

my_list = [{1}] * 10
my_list[0].add(2)
print(my_list)

my_list = [{1} for _ in range(10)]
print(my_list)

# List Comprehension.
# Create a list of squares.
squares = [x * x for x in range(0, 20)]
print(squares)
squares = []
for x in range(0, 20):
    squares.append(x * x)
print(squares)

s = "Hello Kenya"
print(s.upper())
print([t.upper() for t in "Hello Africa"])

# Strip of many commas from the end of strings in alist.
print([w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have, commas,']])

# Organize letters in words more responsibly -in alphabetic order.
sentence = "Handsome is better than ugly"
print(["".join(sorted(word, key=lambda x: x.lower())) for word in sentence.split()])

from random import  randrange
print(randrange(1, 7) for _ in range)

# Conditional List Comprehensions.


