def StringIO():
    import io
    assert io.open is open
    buffer = io.StringIO()
    buffer.write('hello, ')
    buffer.write('world!/n')
    print(buffer.getvalue())
with open('Input Output FIle.py') as f:
    first_line = next(f)
    assert type(first_line) is str
with open('Input Output FIle.py', 'rb') as f:
    first_kb = f.read(1024)
    assert type(first_kb) is bytes
import sys
char_count = sys.stdout.write('hello world?\\n')
print(char_count)

"""
d = {'a': 0, 'b': 1, 'c': 2, '!':3}
for key in d.keys():
    if key.isalpha():
        del d[key]
"""
# hasattr function bug in Python 2
class A(object):
    @property
    def get(self):
        raise IOError
class B(object):
    @property
    def get(self):
        return 'get in b'
a = A()
b = B()


try:
    a.get
except IOError:
    print("no property")






# Abstract Syntax tree.
import ast
import sys
""" The data we collect. Each key is a function name; each value is a dict
with keys: firstline, sigend, docend, and lastline and values of line numbers
where that happens. """
functions = {}
def process(function):
    """Handle the function data stored in function"""
    for funcname, data in functions.items():
        print("function:", funcname)
        print("\tstarts at line:", data['firstline'])
        print("\tsignature ends at line:", data['sigend'])
        if (data['sigend'] < data['docend']):
            print("\tdocstring ends at line:", data['docend'])
        else:
            print("\tno docstring")
        print("\tfunction nds at line:", data['lastline'])
        print()
class FuncLister(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        """ Recursively visit all functions, determining where each function
        starts, where its signature ends, where the docstring ends, and where
        the function ends. """
        functions[node.name] = {'firstline': node.lineno}
        sigend = max(node.lineno, lastline(node.args))
        functions[node.name]['sigend'] = sigend
        docstring = ast.get_docstring(node)
        docstringlength = len(docstring.split('\n')) if docstring else -1
        functions[node.name]['docend'] = sigend + docstringlength
        functions[node.name]['lastline'] = lastline(node)
        self.generic_visit(node)

    def lastline(node):
        """ Recursively find the last line of a node """
        return max([node.lineno if hasattr(node, 'lineno') else -1, ]
                   + [lastline(child) for child in ast.iter_child_nodes(node)])

    def readin(pythonfilename):
        """ Read the file name and store the function data into functions. """

    with open(pythonfilename) as f:
        code = f.read()
    FuncLister().visit(ast.parse(code))

    def analyze(file, process):
        """ Read the file and process the function data. """

        readin(file)
        process(functions)
if __name__ == '__main__':
    if len(sys.argv)>1:
        for file in sys.argv[1:]:
            analyze(file,process)
    else:
        analyze(sys.argv[0],process)








# String boolen
class Myclass:
    def __bool__(self):
        return False
my_instance = Myclass()
print(bool(Myclass))
print(bool(my_instance))