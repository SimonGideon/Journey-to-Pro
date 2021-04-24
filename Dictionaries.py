# Avoiding KeyError Exceptions
mydict = {}
print(mydict)
print(mydict.get("foo", "bar"))
print(mydict)
print(mydict.setdefault("foo", "bar"))
# Iterating Over a Dictionary.
d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])

    # Dictionaries with default values.
from collections import defaultdict
d = defaultdict(int)
d['Key']
d['Key'] = 5
d['Key']

d = defaultdict(lambda: 'empty')
d['Key']
d['Key'] = 'full'
d['Key']


# Merging dictionaries.
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
from collections import ChainMap
print(dict(ChainMap(fish, dog)))
fish.update(dog)
print(fish)

# Accessing keys and Values.
mydict = {
    'a': '1',
    'b': '2'
}
print(mydict)
print(mydict.values())
print(mydict.items())

dictionary = {"Hello": 1234, "World": 5678}
print(dictionary["Hello"])
w = dictionary.get("whatever")
x = dictionary.get("whatever", "nuh-uh")
mylist = [x, w]
for i in mylist:
    print(i)
# Creating a dictionary.
stock = {'eggs': 5, 'milk': 2}
"""Creating and populating it 
with values"""
dictionary = {}
# Creating an empty dictionary.


# Populating it.
dictionary['eggs'] = 5
dictionary['milk'] = 2

# The value can also be lists.
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}

# Adding new elements to the values list.
mydict['a'].append(4)
mydict['b'].append('four')
print(mydict.items())

# Create a dictionary using a list of two-items tuples.
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterable)
print(dictionary)

# Using keyword argument:
dictionary = dict(eggs=5, milk=2)
print(dictionary)


# Use of dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'))
print(dictionary)
dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5))
print(dictionary)


# Creating an ordered dictionar.
from collections import OrderedDict

d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4

print(d)
for key in d:
    print(key, d[key])


# Unpacking dictionaries using the **operator.
def parrot(voltage, state,action):
    print("This parrot wouldn't", action, end='')
    print("if you put", voltage, "volts through it.", end='')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# The trailing comma.
role ={"By day": "A typical programmer",
       "By night": "Still a typical programmer", }
print(role)


# The dict() constructor.
dict(a=1, b=2, c=3)
print(dict([('d', 4), ('e', 5), ('f', 6)]))
print(dict([('a', 1)], b=2, c=3))
dict({'a' : 1, 'b' : 2}, c=3)



# Dictionaries Example.
car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
print("Little" " "+ car["color"] + " " + car["model"] + "!")



# All combination of Dictionary values.
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}
import itertools
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combinations))
for combinations in itertools.product(*values)]
print(combinations)
