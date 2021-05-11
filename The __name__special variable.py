def enter_exit_info(func):
    def wrapper(*arg, **kw):
        print('--entering', func.__name__)
        res = func(*arg, **kw)
        print('__exiting', func.__name__)
        return res
    return wrapper
@enter_exit_info
def f(x):
    print('In:', x)
    res = x + 2
    print('Out:', res)
    return res
a = f(2)

# Checking path existence and Permissions.
import os
path = "/home/myFiles/directory1"
n = os.access(path, os.F_OK)
print(n)



# Creating Python Packages.
from setuptools import setup
setup(
    name='package_name',
    version='0.1',
    description='Visualizstion',
    url='http://facebook.com',
    install_requires=[],

    package=['Package_name']

)

import pip
command = 'install'
parameter = 'selenium'
second_param = 'numpy'
switch = '--upgrade'
pip.main([command, parameter, second_param, switch])

# Handling import error
if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print("To use this module you need 'requests' module")
        t = input('Install requests? y/n: ')
        if t == 'y':
            import pip
            pip.main(['install', 'requests'])
            import requests
            import os
            import sys
            pass
        else:
            import os
            import sys
            print('Some functionality can be unavailable.')
else:
    import requests
    import os
    import sys

pip.install --upgrade

# Using commmand line argumnets with arg
import sys
import getpass
word = sys.argv[1:]
sentence = " ".join(words)
print("[%s] %s" % (getpass.getuser(), sentence))
argv = reversed(sys.argv)
argv = argv.pop()
while len(argv) > 0:
    if arg in ('-f', '--foo'):
        print('seen foo!')
    elif argv in ('-b', '--bar'):
        print('seen bar!')
    elif arg in ('-a','--with-arg'):
        arg = arg.pop()
        print('seen value: {}'.format(arg))
    arg = argv.pop()

# Custom parser error message with argparse.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foo")
parser.add_argument("-b", "--bar")
args = parser.parse_args()
if args.foo and args.bar is None:
    parser.error("--foo requires --bar. You did not specify bar.")
print("foo =", args.foo)
print("bar =", args.bar)


# Subprocess Library.
process = subprocess.Popen([your_command], stdout=subprocess.PIPE)
while process.poll() is None:
    output_line = process.stdout.readline()