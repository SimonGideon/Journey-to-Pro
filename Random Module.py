from string import punctuation, ascii_letters, digits
import random
symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols) for i in range(10))
print(password)

import string
def choice():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break


# Create cryptographically secure random numbers.
from random import SystemRandom
secure_rand_gen = SystemRandom()
print([secure_rand_gen.randrange(10) for i in range(10)])

print(secure_rand_gen.randint(0, 20)) # To create a random integer.

# Random and Sequences: Shuffle, choice and sample.
import random
laughs = ["Hi", "Ho", "He", "Huu"]
random.shuffle(laughs)
print(laughs)
print(random.choice(laughs))
print(random.sample(laughs , 1))
print(random.sample(laughs, 3))

# Creating random integers and floats: randint, randrange, random, and uniform.
import random
x = 1
y = 8
random.randint(x, y)
random.randint(1, 8)
# 'random.randrange has the same syntax as range and like random.randint.
random.randrange(100)


random.seed(5) # Create a fixed state.
print(random.randrange(0, 10))
save_state = random.getstate()
print(random.randrange(0, 10))
random.setstate(save_state)
print(random.randrange(0, 10))

# Random Binary Decision
from random import randint
probability = 0.3
if randint(0, 1) < probability:
    print("Decision with probability 0.3")
else:
    print("Decision with probability 0.7")

