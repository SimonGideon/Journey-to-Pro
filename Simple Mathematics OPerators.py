# Division.
from __future__ import division
a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a / b)
print(c / d)
print(a // b)
print(float(c) / b)

import operator # the operator module provides 2 argument arithetic function.
r = operator.truediv(a,  b)
t = operator.floordiv(a, b)
y = operator.floordiv(a, c)

Mylist = [r, t, y]
for S in Mylist:
    print(S)
# Addition.
a, b = 1, 2
print(a + b) # Suing of an operator.

import operator
print(operator.add(a, b))
print(operator.add(a, b))

# Exponentiation.
a, b, c = 2, 15, 4
print(a ** b) # Finding the raised form.
print(pow(a, b))

import math
print(math.pow(a, b))

import operator
print(operator.pow(a, b))
print(pow(2, 15, 4)) # Calculates (2 ** 15) % 4.

# Special function.
import math
import cmath
c =4
print(math.sqrt(c)) # Floats and does not allow complex results.
print(cmath.sqrt(c)) # Allows complex results.

import math
x = 8
print(math.pow(x, 1/3))  # Calculates x raised to 1/3.
print(x**(1/3))

print(math.exp(5)) # Calculates e raised 5.
print(math.expm1(1e-6))

# Trigonometric Functions.
a, b, c, d = 1, 2, 30, 50
import math
print(math.sin(a)) # returns the sin of 'a' in radians.
print(math.cosh(c)) # returns the inversee of hypobolic cosine of 'b' in radians.
print(math.atan(a)) # returns the arc tangent of 'a' in radians.
math.hypot(a, b) # returns the Euclidean norm, same as math.sqrt(a**a + b*b)
print(math.degrees(a)) # Converst from radian to degree.
print(math.radians(57.29577951308232)) # Converts from degree to radian.


# Subraction.
a, b = 1, 2
print(b - a)
import operator
print(operator.sub(b, a))

# Multiplication.
print(a*b)
import operator
print(operator.mul(a, b))

# Logarithms.
import math
import cmath
print(math.log(5))
print(math.log(5, math.e))
print(cmath.log(5))
print(math.log1p(5)) # Logarithm base e - 1
print(math.log2(8)) # Logaritthm base 2.
print(math.log10(100)) # Log base 10.
print(cmath.log10(100))

# Modulus.
"""% is used to display the modulus"""
print(3%  4)

import operator
a = operator.mod(3, 4)
b = operator.mod(10, 2)
c = operator.mod(6, 4)
Mylist = [a, b, c]
for Z in Mylist:
    print(Z)



a / b
