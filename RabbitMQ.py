# How to ocnsume message from RabitMQ
from amqpstorm import connection


def on_message(message):
    """This function is called on message received.
    :param message: Delivered message.
    return:
    """
    print("Message:", message.body)
    # Acknowledge that we handled the message without any issues.
    message.ack()


# Publishing message to Rabbit MQ
from amqpstorm import Connection
from amqpstorm import Message

connection = Connection('127.0.0.1', 'guest', 'guest')
channel = connection.channel()
# Message Properties.
properties = {
    'content_type': 'text/plain',
    'headers': {'key': 'value'}
}


# Create the message.


# Descriptor.
class DescPrinter(object):
    """A data descriptor that logs activity."""
    _val = 7


def __set__(self, obj, val):
    print('Setting', val)
    self._val = val


def __delete__(self, obj):
    print('Deleting ...')
    del self._val


class Foo():
    x = DescPrinter()


i = Foo()
i.x

# Tempfile.
# NamedTemporaryFile
import tempfile
with tempfile.NamedTemporaryFile(delete=False) as t:
    t.write('Hello World!')
    path = t.name
    print(path)
with open(path) as t:
    print(
    t.read())


# Unzipping files.
file_unzip = 'filename.zip'
unzip = zipfile.ZipFile(file_unzip, 'r')
unzip.extractall()
unzip.close()
# Python TarFile.extractall() to decompress a tarball.
file_untar = 'filename.tar.gz'
untar = tarfile.TarFile(file_untar)
untar.extractall()
untar.close()


with zipfile.ZipFile(filename) as zip:
    info = zip.infolist()
    print(zip[0].filename)
    print(zip[0].date_time)
    print(info[0].file_size)


# Opening zip Files.
import zipfile
filename = 'zipfile.zip'
zip = zipfile.ZipFile(filename)
print(zip)
zip.close()
with zipfile.ZipFile(filename, 'r') as z:
    print(zip)

# Getting start with GZip.
import gzip
import os
outfilename = 'example.txt.gz'
output = gzip.open(outfilename, 'wb')
try:
    output.write('Contents of the example file go here.\n')
finally:
    output.close()
print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes of compressed data')
os.system('file -b --mime %s' % outfilename)




