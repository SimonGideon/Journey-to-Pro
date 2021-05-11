class Duck:
    def quack(self):
        print("Quaaaaaack!")

    def feathers(self):
        print("The duck has white and gray feathers.")


class Person:
    def quack(self):
        print("The person imitates a duck.")

    def feathers(self):
        print("The person takes a feather from the ground and shows it.")

    def name(self):
        print("John Smith")

    def in_the_forest(obj):
        obj.quack()
        obj.feathers()


donald = Duck()
john = Person()
in_the_forest(donald)
in_the_forest(john)


# Method Overriding
class Parent(object):
    def introduce(self):
        print("Hello!")

    def print_name(self):
        print("Parent")


class Child(Parent):
    def print_name(self):
        print("Child")


p = Parent
c = Child
p.introduce()
p.print_name()

c.introduce()
c.print_name()


# User defined Methods
class Card:
    special_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

    def __init__(self, suit, pips):
        self.suit = suit

        self.pips = pips


def __str__(self):
    card_name = Card.special_names.get(self.pips, str(self.pips))
    return "%s of %s" % (card_name, self.suit)
def __repr__(self):
    return "Card(%s, %d)" % (self.suit, self.pips
# Debugging.
import pdb
def divide(a, b):
    pdb.set_trace()
    return a/b
print(divide(1, 2))


# Reading and writing with CSV
import pandas as pd
d = {'a': (1, 101), 'b': (2, 202), 'c': (3, 303)}
pd.DataFrame.from_dict(d, orient="index")
df.to_csv("data.csv")