# Breaking loop.
i = 1
while i < 10:
    print(i)
    if i == 4:
        print("Breaking from the loop")
        break
    i += 1
for i in range(0, 10):
    print(i)
    if i == 2:
        break
print("\n")
# Iteration over whole list.
list = ['apha', 'bravo', 'charlie', 'delta', 'echo']
for s in list:
    print(s[:1]) # Prints the first letter.
# for both element and the index of that element.
for idx, s in enumerate(list):
    print("%s has an index of %d" % (s, idx))
print("\n")
# Iterate over sub list.
for i in range(2, 4):
    print("list  at %d contains %s" % (i, list[i]))
for s in list[1::2]:
    print(s)

print("\n")
# While loop.
i = 0
while i < 4:
    #loop statements.
    i = 1 + 1
    break
# while loops runs without condition.
import cmath
complex_num = cmath.sqrt(-1)
while complex_num:
    print(complex_num)
    break
while True:
    print("Infinite loop")
    break

print("\n")
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")

# The pass statement.
x = 15
y = 9
while x == y:
    pass # I don't want to do anything, or are not ready to do anything here, so I'll pass.

# Iterating over dictionaries.
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key)
for key in d.keys():
    print(key)
print("\n")
# To iterate values.
for value in d.values():
    print(value)
# The "half loop" do while
a = 10
while True:
    a = a-1
    print(a)
    if a<7:
        break
print('Done')

print("\n")
# Looping and unpacking.
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for i1, i2, i3 in collection:
    print(i)




print("\n")
# Continue loop.
for i in range(0, 6):
    if i == 2 or i == 4:
        continue
    print(i)



# Continue goes to the next iteration.


# Nested loops.
while True:
    for i in range(1, 5):
        if i == 2:
            break # Will break only in the inner loop.


print("\n")
def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return (i)
        print(i)
    return(5)

for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')


def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
            print(i*j)
# For loops.
for i in range(0, 5):
    print(i)

# Iterating over list.
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

# Loops with an "else" clause.
for i in range(3):
    print(i)
else:
    print('done')


i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')