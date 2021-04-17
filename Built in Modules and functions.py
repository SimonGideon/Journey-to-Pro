print(pow(2, 3))

import math
print(math.sqrt(121)) # Import a builtins function maths to calculate the sqrt.
def sayHello():
    """THis is the function docstring."""
    return 'Hello World'

def sayHello():
    """This is the function docstring."""
    return 'Hello World'

print(str(1356))

# Creating a module
# module created by creating a .py file.
# hello.py
def say_hello():
    print("Hello!")
# aliased modulle
#greet.py
import hello as ai
ai.say_hello()

# module can be stand-alone runnable script.

# run_hello.py
if __name__ == '__main__':
    from hello import say_hello
    say_hello()



