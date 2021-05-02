# Reading a file line -by- line.
with open('Linked List Node.py', 'r') as fp:
    for line in fp:
        print(line)
with open('Linked List Node.py', 'r') as fp:
    while True:
        cur_line = fp.readline()
        if cur_line == '':
            break
        print(cur_line)
with open("Linked List Node.py", "r") as fp:
    line = fp.readline()
for i in range(len(line)):
    print("Line " + str(i) + ": " + line)

# Itterate files (recursively).
"""import os
import pathlib
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)"""

# Getting full content of a file.
with open('Linked List Node.py') as in_file:
    content = in_file.read()
print(content)


# Writing to a file.
with open('Lists_pro.py', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
print(f)


# Random file access using mmap.
"""import mmap
with open('Files & Folders.py', 'r') as fd:
    mm = mmap.mmap(fd.fileno(), 0)
    print(mm.readline())"""

# Replacing text in a file.
import fileinput
replacements = {'Search1': 'Replace1',
                'Search2': 'Replace2'}
for line in fileinput.input('Linked List Node.py', inplace=True):
    for search_for in replacements:
        replace_with = replacements[search_for]
        line = line.replace(search_for, replace_with)
        print(line, end='')
        break
# OS.path.
# Join paths.
import os
os.path.join('a', 'b', 'c')


# Path component Manipulation.
p = os.path.join(os.getcwd(), 'Lists_pro.py')
m = os.path.dirname(p)
n = os.path.basename(p)
o = os.path.split(os.getcwd())
mylist = [p, m, n, o, p]
for i in mylist:
    print(i)

# Get the parent directory.
P = os.path.abspath(os.path.join(PATH_TO_GET_THE_PARENT, os.pardir))
print(P)

# Check if the given path is a directory, file, symbolic link, mount point etc.
filename = dirname + 'main.py'
print(os.path.isfile(filename))
