import winsound

freq = 2500
dur = 1000
winsound.Beep(freq, dur)


class Deque:
    def __init__(self):
        self.items = []


def isEmpty(self):
    return self.items == []


def addFront(self, item):
    self.items.append(item)


def addRear(self, item):
    self.items.insert(0, item)


def removeFront(self):
    return self.items.pop()


def removeRear(self):
    return self.items.pop(0)


def size(self):
    return len(self.items)



# Audio with pyglet
import winsound
freq = 2500
dur = 1000
winsound.Beep(freq, dur)
import pyglet

audio = pyglet.media.load("audio.wav")
audio.play()


# Enum
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    print(Clor.red)
    print(Color(1))
    print(Color['red'])

