from pip._vendor.msgpack.fallback import xrange

foo = 1
bar = 'bar'
baz = 3.14
print('{}, {}'.format(foo, bar, baz))
print('{0}, {1}, {2} and {1}'.format(foo, bar, baz))
print('{0}, {1}, {2}, and {2}'.format(foo, bar, baz))

class AssignmentValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignmentValue(6)
print('My value is: {0.value}'.format(my_value))

# Dictionary keys.
my_dict = {'key': 6, 'other_key': 7}
print("My other key is {0[other_key]}".format(my_dict))
my_list = ['Zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list))
print('{:~^20}'.format('centered'))

# Repetition of arguments.
t = range(0, 30)
print('{0} {2} {6} {8} {4} {4}'.format(*t))

from datetime import datetime, timedelta
once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8, minutes=20)
gen = (once_upon_a_time + x * delta for x in xrange(5))
print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))


# Alignment and padding.
print('{:~<9s}, world'.format('Hello'))
print('{:0=6d}'.format(-123))

# Format literals (f- strings)
foo = 'bar'
print(f'Foo is {foo}')

price = 478.23
print(f"{f'${price:0.2f}':*>20s}")
def fn(l, incr):
    result = l[0]
    l[0] += incr
    return result
lst = [0]
print(f'{fn(lst,2)} {fn(lst, 3)}')

# Floating formatting.
print('{0:.0f}'.format(42.12345))
print('{0:.1f}'.format(42.123456))
import math
n = math.pi
print(n)
print('{:.3f}'.format(n))
print('{0:.3e}'.format(n))
print('{0:.0%}'.format(n))


# Named placeholders.
data = {'first': 'Hilary', 'last': 'May!'}
print('{first} {last}'.format_map(data))

# String formatting with datetime
from datetime import datetime
print('North America:{dt:%m/%d/%Y}. ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()))


# Formatting Numerical Values.
print('{:c}'.format(65)) # Unicode character.

""" Use formatting to conerting an RGB float to avoid hex string:"""
r, g, b = (1.0, 0.4, 0.0)
print('#{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))

# Nested formating.

