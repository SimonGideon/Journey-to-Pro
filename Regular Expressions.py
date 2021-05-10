import re
pattern = r"123"
string = "123zzb"
re.match(pattern, string)
# Out: <_sre.SRE_Match object; span=(0, 3), match='123'>
match = re.match(pattern, string)
print(match.group())

# Searching
pattern = r"(your base)"
sentence = "All your base are belong to us."
match = re.search(pattern, sentence)
match.group(1)
# Out: 'your base'
match = re.search(r"(belong.*)", sentence)
print(match.group(1))

# Replacing
print(re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44"))
# Finding overlaping matches.
results = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
print(results)
# Out: <callable-iterator object at 0x105245890>
for result in results:
    print(result.group(0))
# Matching expressions only in a specific direction.
"""import regex as re
string = "An apple a day keeps the doctor away (I eat an apple everyday)."
rx = re.compile(r'''
\([^()]*\) (*SKIP)(*FAIL) # match anything in parentheses and "throw it away"
| # or
apple # match an apple
''', re.VERBOSE)
apples = rx.findall(string)
print(apples)"""

# Copying data.
d1 = {1:[]}
d2 = d1.copy()
print(d1 is d2)

# Performing a shallow copy.
import copy
c = [[1,2]]
d = copy.copy(c)
print(c is d)

# Copy a set
s1 = {()}
s2 = s1.copy()
print(s1 is s2)

# Context Manager
class AContextManager():
    def __enter__(self):
        print("Entered")
        return "A-instance"
def __exit__(self, exc_type, exc_value, traceback):
    print("Exited" + (" (with an exception)" if exc_type else ""))
# return True if you want to suppress the exception

class MyContextManager:
    def __enter__(self):
        return self
def __exit__(self):
    print('something')

# Assigning to a target.