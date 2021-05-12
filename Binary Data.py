# Formating a list of value into a byte object.
from struct import pack
print(pack('I3c', 123, b'a', b'b', b'c'))


import struct
buffer = struct.pack("hhh", 3, 4, 5)
print("Byte chunk native order:", repr(buffer))

# Idios.
# Dictionary Key initializations.
def add_student():
    try:
        students['count'] += 1
    except KeyError:
        students['count'] = 1
def add_student():
    students['count'] = students.get('count', 0) + 1

# Data serialization.
import json
families = (['John'], ['Mark', 'David', {'name': 'Avraham'}])
# Dumping it into string
json_families = json.dumps(families)
# [["John"], ["Mark", "David", {"name": "Avraham"}]]
# Dumping it to file
with open('families.json', 'w') as json_file:
    json.dump(families, json_file)
# Loading it from string
json_families = json.loads(json_families)
# Loading it from file
with open('families.json', 'r') as json_file:
    json_families = json.load(json_file)

# Multi processing.
import multiprocessing
import time
from random import randint
def countUp():
    i = 0
    while i <= 3:
        print('Up:\t{}'.format(i))
        time.sleep(randint(1, 3))
def countDown():
    i = 3
    while 1 >= 0:
        print('Down:\t{}'.format(i))
        time.sleep(randint(1, 3))
        i-= 1
if __name__ == '__main__':
    workerUp = multiprocessing.Process(target=countUp)
    workerDown = multiprocessing.Process(target=countDown)
    workerUp.start()
    workerDown.start()
    workerUp.join()
    workerDown.join()


