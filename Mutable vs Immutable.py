a = 1
print(id(a))
a += 2
print(a)
print(id(a))
stack = "Overflow"
print(stack)
print(id(stack))
stack += "rocks!"
print(stack)
print(id(stack))

s = ""
for i in range(1, 1000):
    s += str(i)
    s += ","
    print(s)

# Mutable
b = bytearray(b'Stack')
print(b)
b = bytearray(b'Stack')
print(id(b))
b += b'Overflow'
print(b)
print(id(b))

# Config parser
import configparser
config = configparser.ConfigParser()
config['settings']={'resolution':'320x240',
                    'color':'blue'}
with open('example.ini', 'w') as configfile:
    config.write(configfile)
# Pytesseract.
try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
print(pytesseract.image_to_string(Image.open('test.png'), lang='sw'))

# OCR
from PIL import Image
import sys
import pyocr
import pyocr.builders
tools = pyocr.get_available_tools()
# The tools are returned in the recommended order of usage
tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]

# ChemPy - python package
from chempy import Substance
ferricyanide = Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}
print(ferricyanide.unicode_name)

print(ferricyanide.latex_name + ", " + ferricyanide.html_name)

print('%.3f' % ferricyanide.mass)


# Balancing stoichiometry of a chemical reaction
from chempy import balance_stoichiometry # Main reaction in NASA's booster rockets:
reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'})
from pprint import pprint
pprint(reac)
{'Al': 10, 'NH4ClO4': 6}
pprint(prod)
{'Al2O3': 5, 'H2O': 9, 'HCl': 6, 'N2': 3}
from chempy import mass_fractions
for fractions in map(mass_fractions, [reac, prod]):
    pprint({k: '{0:.3g} wt%'.format(v*100) for k, v in fractions.items()})