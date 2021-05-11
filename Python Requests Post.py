# Simple post.
from requests import post
foo = post('http://httpbin.org/post',data= {'key': 'value'})

# Form encoded Data.
from requests import post
payload = {'key1' : 'value1'
           'key2'  'value2'}

# File Upload.
from requests import post
files = {'file': open('data.txt', 'rb')}
foo = post('http://http.org/post', files=files)
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires':
'0'})}
foo = requests.post('http://httpbin.org/post', files=files)

# Distribution
# py2app
import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"
includes = ["atexit",'re']

setup(
    name = application_title,
    version = "0.1",
    description = "Your Description",
    options = {"build_exe" : {"includes" : includes }},
    executables = [Executable(main_python_file, base = base)])

)
# Property Objects
class A:
    p = 1234
    def getX (self):
        return self._x
    def setX (self, value):
        self._x = value
    def getY (self):
        return self._y
    def setY (self, value):
        self._y = 1000 + value

    def getY2(self):
        return self._y
    def setY2 (self, value):
        self._y =value
    def getT (self, value):
        self._t = value
    def setT (self, value):
        self._t = value
    def getU (self):
        return self._u + 10000
    def setU (self, value):
        self._u = value - 5000

    x, y, y2 = property(getX, setX), property (getY, setY), property(getY2, setY2)
    t = property(getT, setT)
    u = property(getU, setU)
A.q = 5678
class B:
    def getZ (self):
        return self.z_
    def setZ (self, value):
        self.z_ = value
    z = property (getZ, setZ)
class C:
    def __init__ (self):
        self.offset = 1234
    def getW (self):
        return self.w_ + self.offset
    def setW (self, value):
        self.w_ = value - self.offset
    w = property (getW, setW)
a1 = A ()
a2 = A ()
a1.y2 = 1000
a2.y2 = 2000
a1.x = 5
a1.y = 6
a2.x = 7
a2.y = 8
a1.t = 77
a1.u = 88
print (a1.x, a1.y, a1.y2)
print (a2.x, a2.y, a2.y2)
print (a1.p, a2.p, a1.q, a2.q)
print (a1.t, a1.u)
b = B ()
c = C ()
b.z = 100100
c.z = 200200
c.w = 300300
print (a1.x, b.z, c.z, c.w)
c.w = 400400
c.z = 500500
b.z = 600600
print(a1.x, b.z, c.z, c.w)