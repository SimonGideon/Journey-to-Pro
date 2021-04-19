# COnditional Expression (or "The Ternary OPraetor")
n = 5
if n >2:
    print("Greater than 2")
else:
    print("Smaller than or equa to 2")

"""Ternary operation 
can also be nested"""
n = 5
if n > 10:
    print("Hello")
else:
    "Goodbye"
if n > 5:
     ""

else:
    print("Good day")

# if, elif, and else.
number = 20
if number > 2:
    print("NUmber bigger than 2")
elif number < 2: # Optional clause one can have mutiple of them.
    print("Number is smaller than 2")
else: #OPtional clause (you can only have one else)
    print("Number is 2")

# Boolean Logic Expression.
# And opearator.
"""returns the last expression if all expressions True;
 first value returns False"""
n = 1 and 2
m = 1 and 0
p = 1 and "Hello World"
Mylist = [n, m, p]
for i in Mylist:
    print(i)

print("" and "Pancakes")

# Or operator.
# Returns the first value that is True.
print(1 or 2)
print(0 or [])


# Lazy evaluation.
def print_me():
    print('I am here!')
print(0 and print_me())

# Testing for mutiple conditions.
a = 1
b = 6
if a > 2 and b > 2:
    print('yes')
else:
    print('no')
"""All expression is true returns the first value
otherwise returns the false value"""
# Each condition should be placed differently to out put the right boolean.
if a == 3 or a == 4 or a == 6:
    print('yes')
else:
    print('no')

# Using 'in' operator.
if a in (3, 4, 6):
    print('yes')
else:
    print('no')


# Else statement.
if True:
    print("It is true")
else:
    print("This wont get printed...")

if False:
    print("This wont get printed...")
else:
    print("It is false!")

# If statement.
if 2 + 2 == 4:
    print("I know math!")
else:
    print("........" * 5)


