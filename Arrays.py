# Access individual element through indexes.
from array import  *

my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[1])
for i in my_array:
    print(i)

# Append any value to the array.
my_array = array('i', [1,2,3,4,5])
my_array.append(6)
print(my_array)

# Insert a value in an array.
my_array.insert(0, 0)
print(my_array)

# Extend python array.
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
print(my_array)

# Add items from list into array.
c = [11,12,13]
my_array.fromlist(c)
print(my_array)

# Remove any array.
my_array.remove(4)
print(my_array)

# Remove last array element.
my_array.pop(1)
print(my_array)

# Fetching an element through its index.
print(my_array.index(5))
print(my_array.index(3))


# Reverse python array.
my_array.reverse()
print(my_array)


# Get array buffer information.
print(my_array.buffer_info())

# Check fo the number of occurrences.
my_array.insert(1, 3)
print(my_array.count(3))

# Converting array to a python list with same element.
my_array.reverse()
c = my_array.tolist()
print(c)

# Append a string to char array.
"""my_char_array = array('c', [g, r, e, e, k])
my_char_array.fromstring("stuff")
print(my_char_array)
"""

# Multi dimensional Array.
# Lists in lists.
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst[0])
print(lst[1])
print(lst[2])

# Accessing different Elements in the list.
print(lst[0][0])
print(lst[1][2])
