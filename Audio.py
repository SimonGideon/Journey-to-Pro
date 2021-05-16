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


# First App
from kivy.app import App
from kivy.uix.label import Label


class Test(App):
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    Test().run()

# Audio with pyglet
import pyglet

audio = pyglet.media.load("audio.wav")
audio.play()
