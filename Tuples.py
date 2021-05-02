t = tuple('lupins')
print(t)
t = tuple(range(3))
print(t)

# Packing and unpacking Tuples.
first, *more, last = (1, 2, 3, 4)
print(first)


# Built in Tuple functions.

t_1 = ('a', 'b', 'c', 'd')
t_2 = ('1', '2', '3')
t_3 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
"""print(cmp(t_1, t_2))"""
print(len(t_1)) # Count tuples


# Converting a list into tuples.
list = [1, 2, 3, 4, 5]
tuple(list)
print(tuple)
print(t_1 + t_2)


# Basic input and output.
print("Output......")

# Input from a file.
"""with open('Heapq.py', 'r') as fileobj:
    content = fileobj.read()
    lines = content.split('\n')
    print(lines)"""


# Read from stdin.
import sys
for line in sys.stdin:
    print(line)
import fileinput
for line in fileinput.input():
    process(line, end= "")

# Using input() and raw_input()
foo = input("Put anything here !!")
print(foo)

# Function to prompt user for a number.
def input_number(msg, err_msg=None):
    while True:
        try:
            return float(raw_input(msg))
        except ValueError:
            if err_msg is not None:
                print(err_msg)
def input_nu_number(msg, err_msg=None):
    while True:
        try:
            return  float(input(msg))
        except ValueError:
            if err_msg is not None:
                print(err_msg)