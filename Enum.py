from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red) # Clor red.
print(Color(1))
print(Color['red'])

# Iteration.
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print([c for c in Color])