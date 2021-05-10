from collections import Counter
c = Counter(["a","b", "c", "d", "a", "b", "c", "d"])
print(c)

# Getting the most common value
from collections import Counter
adict = {'a': 5, 'b': 2, 'e':2, 'q': 5}
print(Counter(adict.values()))

# Counting the occurrence of one item in a sequence.
alist = [1,2,3,4,5,1,2,2,2,4,5,6]
print(alist.count(1))

# The print function.
def sendit(out, *values, sep=' ', end='\n'):
    print(*values, sep=sep, end=end, file=out)