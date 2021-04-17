# Nonlocal Variables.
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()
print(c())
"""'nonlocal' allows assign vrriables in an outer scope
not global scope"""

# Global Variables.
x = 'Hi'
def read_x():
    print(x) # x is just referenced, therefore assumed global.
read_x()


def read_y():
    print(y) # This is just a refrenced therefore assumeb global.
def read_y():
    y = 'Hey' # y appears as an assignmet, local.
    print(y)
read_y()

x = 'Hi'
def change_local_x():
    x = 'Bye'
    print(x)
change_local_x()
print(x)

x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x()
print(x)