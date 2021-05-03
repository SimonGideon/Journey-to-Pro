class Person(object):
    """A simple class"""
    speciies = "Homo Sapiens"  # Class Attribute

    def __init__(self, name):  # Specila method
        """This is the initialzer. It is
        a special method """
        self.name = name

    def __str__(self):
        """Thismethod is run when Python tries to cast the object to a string.
        Return this string when using print()"""
        return self.name

    def rename(self, rename):
        """Reassign and print the name attribute"""
        self.name = rename

        print("Now my name is {}".format(self.name))


# Bound, unbound, and static method.
class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)


s = D.f(12)
n = D.g
p = D.g("World")
for i in [s, n, p]:
    print(i)
d = D()
d.multiplier = 1337
print(D.multiplier, d.multiplier)


# Basic inheritance.
class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, s):
        # Call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s


# Instantiate.
r = Rectangle(3, 4)
s = Square(2)
a = isinstance(r, Rectangle)
b = isinstance(r, Square)
c = isinstance(s, Rectangle)
d = isinstance(s, Square)
for i in [a, b, c, d]:
    print(i)


# MOnkey Patching.
class A(object):
    def __int__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)


# Class method: alternate initializers
class Person(object):
    def __init__(self, firts_name, last_name, age):
        self.first_name = firts_name
        self.last_name = last_name
        self.age = age
        self.full_name = firts_name + "" + last_name


@classmethod
def from_full_name(cls, name, age):
    if "" not in name:
        raise ValueError
    first_name, last_name = name.split(" ", 2)
    return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


bob = Person("Bob", "Bobberson", 42)
alice = Person("Alice", "Henderson", 31)


# Multiple Inheritance.
class Foo(object):
    def __init__(self):
        print("foo init")


class Bar(object):
    def __init__(self):
        print("bar init")


class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()


a = FooBar()

print(isinstance(a, FooBar))
print(isinstance(a, Foo))


# Properties.
class Character(object):
    def __init__(self, name, max_hp):
        self.first_name = name
        self._hp = max_hp
        self._max_hp = max_hp
        self._max_hp = max_hp

    @property
    def hp(self):
        return self._hp

    # Make name read by not only by not providing a set method.
    @property
    def name(self):
        return self.name

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = 0 if self.hp < 0 else self.hp

    @property
    def is_alive(self):
        return self.hp < self.max_hp if self.hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive


bibo = Character('Bilbo Baggins', 100)
print(bibo.hp)


# Default value for instance variables.
class Rectangle2D(object):
    def __init__(self, width, height, pos=[0, 0], color='blue'):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color


r1 = Rectangle2D(5, 3)
r2 = Rectangle2D(7, 8)
r1.pos[0] = 4
print(r1.pos)
print(r2.pos)


# Class and Instance variables.
class c:
    x = 2  # Class variable

    def __init__(self, y):
        self.y = y  # Instance variable


print(c.x)

c1 = c(3)
print(c1.x)
c2 = c(4)
print(c2.x)


class D:
    x = []

    def __init__(self, item):
        self.x.append(item)  # note that this is not an assgnment!


d1 = D(1)
d2 = D(2)

print(d1.x)
print(d2.x)


# Class compodition.
class County(object):
    def __init__(self):
        self.cities = []

    def addCity(self, city):
        self.cities.append(city)


class City(object):
    def __init__(self, numPeople):
        self.people = []
        self.numPeople = numPeople


def addPerson(self, person):
    self.people.append(person)


def join_country(self, country):
    self.country = country
    country.addCity(self)

    for i in range(self.numPeople):
        person(i).join_city(self)

        class Person(object):
            def __init__(self, ID):
                self.ID = ID

            def join_city(self, city):
                self.city = city
                city.addPErson(self)

            def people_in_my_country(self):
                x = sum([len(c.people) for c in self.country.cities])
                return x


"""US = County()
NYC = City(10).join_country(US)
SF = City(5).join_country(US)
print(US.cities[0].people[0].people_in_my_country())
"""
# Listing All Class MEmbers.
print(dir(list))


# Singleton Class.
class Singleton:
    def __init__(self, decorated):
        self.__decoratef = decorated


def Instance(self):
    try:
        return self.__instance
    except AttributeError:
        self.__instance = self._decorated()
        return self.__instance

    def __call__(self):
        raise TypeError('Singletons must be acceesed through Instance()')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Single:
    def __init__(self):
        self.name = None
        self.val = 0

    def getName(self):
        print(self.name)


x = Single.Instance()
y = Single.Instance()
x.name = 'I\'m single'
print(x.getName())
