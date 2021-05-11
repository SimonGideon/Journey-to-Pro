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
