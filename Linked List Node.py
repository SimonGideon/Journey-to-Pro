class Node:
class Node:
    def __init__(self, cargo=None, next=None):
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.car = cargo
        self.cdr = next
        self.cdr = next
    def __str__(self, car):
    def __str__(self, car):
        return str(self.car)
        return str(self.car)
    def display(lst):
    def display(lst):
        if lst:
        if lst:
            w("%s" % lst)
            w("%s" % lst)
            print(lst.cdr)
            print(lst.cdr)
        else:
        else:
            print(w("ni\n"))
            print(w("ni\n"))


"""break"""
"""break"""


# Filter
# Filter
names = ['Fred', 'Wilma', 'Barney']
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
def long_name(name):
    return len(name) > 5
    return len(name) > 5
print(filter(long_name, names))
print(filter(long_name, names))
print(
print(
    list(filter(long_name, names))
    list(filter(long_name, names))
)
)
# Filter without function
# Filter without function
print(
print(
list(filter(None, [1, 0, 2, [], '', 'a']))
list(filter(None, [1, 0, 2, [], '', 'a']))
)
)


# Filter as short circuit check.
# Filter as short circuit check.
"""car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 500)]
"""car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 500)]
def find_something_smaller_than(name_value_tuple):
def find_something_smaller_than(name_value_tuple):
    print('check {0}, {1}$'.format(*name_value_tuple)
    print('check {0}, {1}$'.format(*name_value_tuple)
    return name_value_tuple[1] < 100
    return name_value_tuple[1] < 100
    next(filter(find_something_smaller_than, car_shop))
    next(filter(find_something_smaller_than, car_shop))
    )"""
    )"""


break
break


# Complementary function: filterfalse, ifilterfalse.
# Complementary function: filterfalse, ifilterfalse.
from itertools import filterfalse
from itertools import filterfalse
list(filterfalse(None, [1, 0, 2, [], '', 'a']))
list(filterfalse(None, [1, 0, 2, [], '', 'a']))




# Usage with function.
# Usage with function.
names = ['Fred', 'Wilma', 'Barney']
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
def long_name(name):
    return len(name) > 5
    return len(name) > 5
print(list(filterfalse(long_name, names))
print(list(filterfalse(long_name, names))


