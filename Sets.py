# Operations on sets.
# Intersection
r = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
print(r)
s = {1, 2, 3, 4, 5} & {3, 4, 5, 6}
print(s)

# Union
a = {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
b = {1, 2, 3, 4, 5, 6} | {3, 4, 5, 6}
Mylist = [a,b]
for i in Mylist:
    print(i)
# Difference.
x = {1, 2, 3, 4, 5}.difference({2, 3, 5})
y = {1, 2, 3, 4, 5, 9, 5} - {2, 3,5}
Mylist = [x, y]
for z in Mylist:
    print(z)

# Symetric difference with.
d = {1, 2, 3, 4}.symmetric_difference({2, 3, 4})
e = {1, 2, 3, 3, 4} ^ {2, 3, 5}

# Super set check
f = {1, 2}.issuperset({1, 2, 3})
g = {1, 2} >= {1, 2, 3}

# Superset check.
h = {1, 2}.issubset({1, 2, 3})
i = {1, 2} <= {1, 2, 3}

Mylist = [d, e, f, g, h, i]
for q in Mylist:
    print(q)
# Disjoint check.
a = {1, 2}.isdisjoint({3, 4})
b = {1, 2}.isdisjoint({1, 4})
print(a)
print(b)

# Existance check.
print(2 in {1, 2, 3})
print(4 in (2, 4, 5, 9, 0))
print(0 in (6, 4, 7, 3))

# Add and remove
s = {1, 2, 3}
s.add(4)
print(s)

s.discard(3)
print(s)
s.remove(2)
print(2)

s = {1, 2}
s.update({3, 4})
print(s)

# Get the unique element of a list.
restaurants = ["McDonald", "Five Star", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
print(list(unique_restaurants))

print(list(set(restaurants)))

# Sets of sets.
s = {frozenset({1, 2}), frozenset({3, 4})}
print(s)

# Set Operations using Method and Builtins.
a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}

# Intersection
print(a.intersection(b))

# Union.
print(a.union(b))

# Diference.
print(a.difference(b))

# symetric difference.
print(a.symmetric_difference(b))

# symetric diffrence(b) == symetric difference(a).

# Subset and superset.
c = {1, 2}
print(c.issubset(a))
print(a.issuperset(c))

# Disjoint.
d = {5, 6}
print(a.isdisjoint(d))
print(a.isdisjoint(d))

# Testing Membership.
p = 1 in a
t = 6 in d
print(p, t)

# Length.
print(len(a))
Mylist = [a, b, c, d]
for Z in Mylist:
    print(len(Z))

# Sets versus multisets.
A = ['a', 'b', 'b', 'c']
print(A)
from collections import Counter
counterA = Counter(['a', 'b', 'b', 'c'])
print(counterA)
