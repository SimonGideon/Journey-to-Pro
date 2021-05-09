import random
print(random.randint(1, 10))


import random as rn
print(rn.randint(1, 10))

from math import sin
print(sin(1))

from urllib.request import urlopen
import time, socket, random
from math import sin, cos, tan, pi
print(cos(45))
print(pi)
print(time.time())
from math import *

# Importing modules from an arbitrary filesystem location.
"""This  can be done adding the path ti the directory where your module is found to sys path
"""

"""import sys
sys.path.append("path here")
import module"""

# Importing all names from all names from a module.
from math import *
print(sqrt(2))
print(ceil(2.7))


# Programmatic importing.
import importlib
random = importlib.import_module("random")


# Importing specific names from module.
from random import randint
print(randint(1, 10))


# Importing submodules.
"""from module.submodule import function"""

# Reimporting a module.
import math
math.pi = 3

print(math.pi)
import sys
if 'math' in sys.modules:
    del sys.modules['math']
import math
print(math.pi)


