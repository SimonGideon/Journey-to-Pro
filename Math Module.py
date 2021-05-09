# Rounding: round, floor, ceil, trunc
x = 1.55
y = -1.55
print(x)
print(round(y))
print(round(x, 1))
print(round(y, 1))


import math
print(math.floor(x)) # To gt the largest integer less than X

print(math.ceil(x)) # To greater the smallest integer greater than x

# Droping fractional part of X.

print(math.trunc(x))

# Trigonometry.
print(math.hypot(2, 4))

# Converting degrees into a radian.
print(math.radians(45))

# Convert the result of a sin to degrees.
print(math.degrees(math.asin(1)))

# Hyperbolic isne, cosine and tangent
print(math.sinh(math.pi)) # Hyperbolic of sin function

print(math.cosh(math.pi))  # Hyperbolic cosine function.


# Pow for faster exponentiation
from math import pow
print(pow(5, 5))

# Infinity and NaN("not a number")
pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan
print(pos_inf, neg_inf, not_a_num)

print(math.isfinite(0.0))

import sys
print(sys.float_info.max)

# Logarithms.


