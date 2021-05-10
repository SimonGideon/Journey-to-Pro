#  Basic deque using
from collections import deque

d = deque([1, 2, 3])
p = d.popleft()
print(d.appendleft(0))

# Limit deque size
from collections import deque

d = deque(maxlen=3)
print(d.append(1))
print(d.append(2))

# Breadth First Search
from collections import deque


def bsf(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        current = q.popleft()
        for neighbour in graph[current]:
            if neighbour not in distances:
                distances[neighbour] = distances[current] + 1
                q.append(neighbour)
    return distances


graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}

# Open a URL with Default Browser.
import webbrowser

webbrowser.open("http://stackoverflow.com")

# Opening a URL with Different Browsers.
import webbrowser

"""ff_path = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
ff.open("http://stackflow.com")

# Registering a browser type:
import webbrowser
ff_path = webbrowser.get("C: Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
webbrowser.register('firefox', None, ff)
webbrowser.get('firefox').open("https://stackoverflow.com/")
"""

# tkinter
from tkinter import *


class PlaceExample(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        top_text = Label(master, text="This is on top the origin")
        top_text.place(x=0, y=0, height=50, width=200)
        bottom_right_text = Label(master, text="This is at position 200, 400")
        bottom_right_text.place(x=200, y=400, height=50, width=200)

    if __name__ == "__name___":
        root = Tk()
        place_frame = PlaceExample(root)
        place_frame.mainloop()


# from tkinter import *
class GridExample(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        top_text = Label(self, text="This text appears on top left")
        top_text.grid()
        bottom_text = Label(self, text="This text appears on bottom left")
        bottom_text.grid()
        right_text = Label(self, text="This text appears on the right and spans both rows",
                           wraplength=100)
        right_text.grid(row=0, column=1, rowspan=2)


if __name__ == "__main__":
    root = Tk()
    grid_frame = GridExample(root)
    grid_frame.mainloop()
# Making shallow copy of an array.
arr = ['a', 'b', 'c']
copy = arr[:]
arr.append('d')
print(arr)
print(copy)


class MultiIndexingList:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.value[item])
        return [self.value[i] for i in item]

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.value[item] = value
        elif isinstance(item, int):
            raise ValueError('Cannot interpret slice with multiindexing')
        else:
            for i in item:
                if isinstance(i, slice):
                    raise ValueError('Cannot interpret slice with multiindexing')
                self.value[i] = value

    def __delitem__(self, item):
        if isinstance(item, int):
            del self.value[item]
        elif isinstance(item, slice):
            del self.value[item]
        else:
            if any(isinstance(elem, slice) for elem in item):
                raise ValueError('Canot interpret slice with multiindexing')
            item = sorted(item, reverse=True)
            for elem in item:
                del self.value[elem]


a = MultiIndexingList([1, 2, 3, 4, 5., 6, 7, 8])
print(a)

# Plotting with Matplotlib.
# Plots with Common X-axis but different Y-axis; using twinx()
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0 * npi, 101)
y = np.sin(x)
z = np.sinh(x)
fig, ax1 = plt.subplots()
ax2 = ax1 = plt.subplots()
ax2 = ax1.twinx()
curve1, = ax1.plot(x, y, label="sin", color='r')
curve2, = ax2.plot(x, z, label="sinh", color='b')
curves = [curve1, curve2]
ax1.legend(curves, [curve.get_label() for curve in curve])
plt.title("Plot of sine and hyperbolic sine")
plt.show()

# A simple Plot in Matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2, 0*np.pi, 101)
y = np.sin(x)
plt.plot(x, y)
plt.show()
