# Appending a string as a new line.
def append_to_csv(input_string):
    with open("fileName.csv", "a") as csv_file:
        csv_file.write(input_row + "\n")

# Evaluation a string containing a Python literal with ast.literal_eval.
"""import ast
code = (1, 2, ('foo': 'bar'}))
object = ast.literal_eval(code)
print(object)
type(object)"""
# Data Visualization with Python.
import numpy as np
import seaborn as sns
data = np.random.randn(1000)
sns.distplot(data, kde=True, rug=True)

import matplot.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6]
y = [i**2 for i in x]
plt.scatter(x, y, c='blue', marker='x', s=100)
plt.plot(x, y, color='red', linewidth=2)
plt.xlabel('x data')
plt.ylabel('y data')
plt.title('An example plot')
plt.show()

# MayaVI
from numpy import sin, cos, mgrid, pi, sqrt
from mayavi import mlab
mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
u, v = mgrid[-0.01, -0.035:pi:0.01]
x = 2 / 3.* (cos(u) * cos(2    * v)
             + sqrt(2) * sin(u) * cos(v)) * cos(u) / (sqrt(2) - sin(2 * u) * sin(3 * v))
y  = 2 / 3.* (cos(u) * sin(2 * v) - sqrt(2) * sin(u) * sin(v)) * cos(u) / (sqrt(2) - sin(2 * u) * sin(3 * v))
Z = -sqrt(2) * cos(u) * cos(u) / (sqrt(2) - sin(2 * u) * sin(3 * v))
S = sin(u)
mlab.mesh(X, Y, Z, scalars=S, colormap='YlGnBu', )
mlab.view(.0, - 5.0, 4)
mlab.show()

# *args and **kwargs
def print_kwargs(**kwargs):
    print(kwargs)

# Using *ags when writing functions.
def print_args(farg, *args):
    print("format arg: %s" % farg)
    for arg in args:
        print("another positional arg: %s" % arg)
print_args(1, "two", 3)

# Using **kwargs when calling functions.
def test_func(arg1, arg2, arg3):
    print("arg1: %s" % arg1)
    print("arg2: %s" % arg2)
    print("arg3: %s" % arg3)
kwargs = {"arg3": 3, "arg2": "two"}

# Reuse of primitive objects.
import sys
sys.getrefcount(1)
a = 1
b = 1
print(sys.getrefcount(1))
