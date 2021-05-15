import serial
ser = serial('/dev/ttyUSB0', 9600)
# to read a single byte
data = ser.read()


# Neo4j and Cypher using Py2Neo.
results = News.objects.todays_news()
for r in results:
    article = graph.merge_one("NewsArticle", "news_id", r)
    if 'LOCATION' in results[r].keys():
        for loc in results[r]['LOCATION']:
            loc = graph.merge_one("Location", "name", loc)
            try:
                rel = graph.create_unique(Relationship(article, "about_place", loc))
            except Exceptione:
                print(e)

# Autocomplete on News Title
def get_auticomplete(text):
    query = """
    start n = node(*) where n.name =~ '(?i)%s.*' return n.name,labels(n) limit 10;
    """
    query = query % (text)
    obj = []
    for res in graph.cypher.executed(query):
        obj.append({'name':res[0],'entity_type':res[1]})
        return res

#Templets in python
from string import Template
data = dict(item = "candy", price = 8, qty = 2)
t = Template("Simon bought $qty $item for $price dollar")
print(t.substitute(data))

# Changing delimiter
from string import Template
class MyOtherTemplate(Template):
    delimiter = '#'
data = dict(id = 1, name = "Ricardo")
t = MyOtherTemple("My name is #Name and I have the id: #id")
print(t.substitute(data))


# Pillow.
# Read image file.
from PIL import Image
im = Image.open("Image.bmp")



# Convert files to JPEG
from__future__import.print_function
import os, sys
from PIL import Image
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("Cannot convert".infile)

# The pass statement.
# ignore an exception
try:
    metadata = metadata['properties']
except KeyError:
    pass


# Creating a new Exception that can be caught
class CompileError(Exception):
    pass

# argparse(default help formatter.
import argparse
import sys

def check():
    print("status")
    return 0
parser = argparse.ArgumentParser(prog="sub", add_help=False)
subparser = parser.add_subparsers(dest="cmd")
subparser.add_parser('status', help='show status')
subparser.add_parser('list', help='print list')
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)
args = parser.parse_args()
if args.cmd == 'list':
    print('list')
elif args.cmd == 'status':
    sys.exit(check())

