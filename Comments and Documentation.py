def func():
    """This is a function that does nothig at all"""
    return
print(func.__doc__)
def greet(name, geeting="Hello"):
    """Print a greeting to the user 'name'
    optional parameter 'greetings' can change what they're greeded with"""
    print("{} {}".format(greeting, name))
help(greet)
print(greet.__doc__)

# Documentation using doc string.
def hello (name):
    """Greet someone.

    print s greeting ("Hello") for the person with the given name.
    """
    print("Hello "+name)
class Greetier:
    """Anobject used to greet people.
    It contains mutiple greeting function for several languages
    and times of the day.
    """
# Syntax conventions.
def hello():
    """Say hello to your friends."""
    print("Hello my friends!")



# Sphinx
def hello(name, language="en"):
    """Say hello to a person.

    :param name: the name of the person
    :type name: str
    :param language: the language in which the person should be greeted
    :type language: str
    : return: a number
    : rtype: int
    """

