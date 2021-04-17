print(~-0)
print(~-1)
print(~-123)
print(60 ^ 30)
# Bitwise XOR (Exclusive OR).
print(bin(60 ^ 30))

# Bitwise AND.
print(60 & 30)
print(bin(60 & 30))

# Bitwise OR.
print(60 | 30)
print(bin(60 | 30))

# Bitwise Left Shift.
print(2 << 2)
print(bin(2 << 2))
print(7 << 1)
# The same as 2**n:

# Bitwise Right Shift.
a = 8 >> 2
b = bin(2 >> 2)
Mylist = [a, b]
for I in Mylist:
    print(I)
# This is equivalent to integer division 2.


# Inplace Operations.
a = 0b001
print(a)
a &= 0b010
print(a)

