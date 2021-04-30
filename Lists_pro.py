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

# Conditional List Comprehensions.
print([x for x in range(10) if x % 2 == 0])

even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)
        print(even_numbers)
numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)
print(numbers)

# Merging Dictionary.
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
print({k: v for d in [dict1, dict2] for k, v in d.items()})

# Comprehension with NEsted Loops.
data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
        break
print(output)

# Generator Expressions.

for i in (x ** 2 for x in range(10)):
    print(i)

# Setting Comprehensions.
text = "when in the Course of human event it becomes necessary for one people...."
print({ch.lower() for ch in text if ch.isalpha()})

# Refactoring filter and map to list comprehension.
# map & Filter
filtered = filter(lambda x: x % 2 == 0, range(10))
results = map(lambda x: 2 * x, filtered)

# List comprehension
results = [2 * x for x in range(10) if x % 2 == 0]

print(results)

# Comprehensions involving tuples.
print([x + y for x, y in [(1, 2), (3, 4), (5, 6)]])

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x + y)

# Counting Occurrences Using Comprehension.
"""Count the numbers in range(1000) 
       that are even and contain the digit '9' """
print(sum(
    1 for x in range(1000)
    if x % 2 == 0 and
    '9' in str(x)
))

# Changing the Types in a list.
# Convert a list of strings into an integer.
items = ["1", "2", "3", "4"]
print([int(item) for item in items])

# Convert a list of strings to float.
items = ["1", "2", "3", "4"]
print(map(float, items))

# Nested List Comprehensions.
# List comprehension with nested loop.
print([x + y for x in [1, 2, 3] for y in [3, 4, 5]])
# Nested List Comprehension.
print([[x + y for x in [1, 2, 3]] for y in [3, 4, 5]])

matric = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print([[row[i] for row in matric] for i in range(len(matric))])

# Iteration two or more list simultaneously within list comprehension.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['6', '7', '8', '9']
print([(i, j) for i, j in zip(list1, list2)])
[(i, j, k) for i, j, k in zip(list1, list2, list3)]

# List Slicing (Selecting parts of the list).
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[::2])
print(lst[::3])

# Selecting a sublist from a list.
print(lst[2:4])
print(lst[2:])
print(lst[:4])

# Reversing a list with slicing.
b = lst[::-1]
print(b)

# Shifting a list using slicing.
"""def shift_list(array, s):
    s %=len(array) # To calculate the actual shift amount.
    S *= -1 # Reverse the shift direction.
    shifted_array = array[s:] + array[:s]
    return shifted_array
my_array = [1, 2, 3, 4, 5]
shift_list(my_array, -7) # negative number
shift_list(my_array, 5) # no shift on number to the six=ze of the array
shift_list(my_array, 3)"""

# Groupby().
import itertools
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"), ("vehicle", "speed boat"),
          ("vehicle", "school bus")]
dic = {}
f = lambda x: x[0]
for key, group in itertools.groupby(sorted(things, key=f), f):
    # dic[key] = list(group)
    dic
list_things = ['goat', 'dog', 'donkey','mulato', 'cow', 'cat', ('persons', 'man', 'woman'), 'wombat', 'mangoose',
               'maloo', 'camel']
c = itertools.groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)


# Linked lists.
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self):
        self.data = val
    def  LinkedList:
        def __init__(self):
            self.head = head = None
    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None
    def __add__(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
    def size(self):
        """Return the length/size of the list"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        """Search for item in list. If found, return True. If not found, return False"""
        current = self.head
        found = False
        while current is not NOne and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                return found
    def remove(self, item):
        """Remove item from list. If is not found in list, raise ValueError"""
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if found:
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
            else:
                raise ValueError
                print('Value not found')

    def insert(self, position, item):
        """
        Insert item at position specified. If position specified is
        out of bounds, raise IndexError
        """

    if position > self.size() - 1:
        raise IndexError
    print
    "Index out of bounds."
    current = self.head
    previous = None
    pos = 0
    if position is 0:
        self.add(item)
    else:
        new_node = Node(item)
    while pos < position:
        pos += 1
    previous = current
    current = current.getNext()
    previous.setNext(new_node)
    new_node.setNext(current)

    def index(self, item):
        """
        Return the index where item is found.
        If item is not found, return None.
        """

    current = self.head
    pos = 0
    found = False
    while current is not None and not found:
        if current.getData() is item:
            found = True
    else:
        current = current.getNext()
    pos += 1
    if found:
        pass
    else:
        pos = NoneGoalKicker.com – Python® Notes
    for Professionals 151
        return pos

    def pop(self, position=None):
        """
        If no argument is provided, return and remove the item at the head.
        If position is provided, return and remove the item at that position.
        If index is out of bounds, raise IndexError
        """

    if position > self.size():
        print
        'Index out of bounds'
    raise IndexError
    current = self.head
    if position is None:
        ret = current.getData()
    self.head = current.getNext()
    else:
    pos = 0
    previous = None
    while pos < position:
        previous = current
    current = current.getNext()
    pos += 1
    ret = current.getData()
    previous.setNext(current.getNext())
    print
    ret
    return ret

    def append(self, item):
    # Append item to the end of the list"""
    current = self.head
    previous = None
    pos = 0
    length = self.size()
    while pos < length:
        previous = current
    current = current.getNext()
    pos += 1
    new_node = Node(item)
    if previous is None:
        new_node.setNext(current)
    self.head = new_node
    else:
    previous.setNext(new_node)

    def printList(self):
        """Print the list"""

    current = self.head
    while current is not None:
        print(current.getData())
    current = current.getNext()