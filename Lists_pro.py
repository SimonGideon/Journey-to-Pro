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
people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)
people.sort(key=by_salary)


list_of_tuples = [(1,2), (3,4), (5,0)]
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

