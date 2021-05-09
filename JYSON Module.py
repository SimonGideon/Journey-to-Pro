# Storing Data in a file.
"""import json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}
with open(filename, 'w') as f:
    json.dump(d, f)

# Retrieving data from a file.
import json
with open(filename, 'r') as f:
    d = json.load(f)
"""
# Formatting JSON output.
import json
data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
print(json.dumps(data, indent=2))

# Sorting keays Alphabetically.
print(json.dumps(data, sort_keys=True))

# Getting rid of white space to get compact output.
print(json.dumps(data, separators=(',',':')))

# Load vs loads, dump vs dumps
import json
data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data)
print(json_string)
print(json.loads(json_string))



# JSON encoding custom objects.
import json

from datetime import datetime

class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.isoformat()
        except AttributeError:
            return super(DatetimeJSONEncoder, self).default(obj)
encoder = DatetimeJSONEncoder()
print(encoder.encode(data))
# Creating JSON from Python dict.
import json
d = {
    'foo': 'bar',
    'alice':1,
    'wonderland': [1, 2, 3]

}
json.dumps(d)

