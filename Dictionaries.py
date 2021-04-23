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
