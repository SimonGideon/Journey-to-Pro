# Simple Operator Precedence.
"""Follows PEMDAS Parentheses, Exponents, Mutiplication and Division,
and Addition and Subtraction"""
a, b, c, d = 2, 3, 5, 7
t = a ** (b + c) # parantheses
print(t)

x = a * b ** c # exponent first.
print(x)
y = a + b * c / d # multiplication / division:
print(y)

# Bodmas still stands.
print(300 / 300 * 200)

