class Node:
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next
    def __str__(self, car):
        return str(self.car)
    def display(lst):
        if lst:
            w("%s" % lst)
            print(lst.cdr)
        else:
            print(w("ni\n"))

"""break"""

# Filter
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
    return len(name) > 5
print(filter(long_name, names))
print(
    list(filter(long_name, names))
)
# Filter without function
print(
list(filter(None, [1, 0, 2, [], '', 'a']))
)

# Filter as short circuit check.
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 500)]
def find_something_smaller_than(name_value_tuple):
    print('check {0}, {1}$'.format(*name_value_tuple)
    return name_value_tuple[1] < 100
    next(filter(find_something_smaller_than, car_shop))
    )

    break

# Complementary function: filterfalse, ifilterfalse.
from itertools import filterfalse
list(filterfalse(None, [1, 0, 2, [], '', 'a']))


# Usage with function.
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
    return len(name) > 5
print(list(filterfalse(long_name, names))
