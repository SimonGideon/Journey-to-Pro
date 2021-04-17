# Time between two dates.
from datetime import datetime
a = datetime(2016,10,0o6,0,0,0)
b = datetime(2016,10,0o1,23,59,59)
print(a-b)

# Output datetime to string
from datetime import datetime
datetime_for_string = datetime(2016, 10, 1, 0, 0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
print(datetime.strftime(datetime_for_string, datetime_string_format))

# Parsing string to datetime object.
from datetime import datetime
datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
print(datetime.strptime(datetime_string, datetime_string_format))

print(complex(3))

