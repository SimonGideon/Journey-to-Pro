import datetime
x = datetime.datetime.now()
print(x) # Returns year, mont, day, hour, minute, second and microsecond.
print(x.year) #Out put the current year.
print(x.strftime("%A")) # Outputs the th current day.

#Creating Date Objects.
import datetime
dt = datetime.datetime(2021, 4, 14)
print(dt)

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) # Out put the month of the given date.

# Constructing timezone-aware datetimes.
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
dst = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.tzname())

# COmputing time difference
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
delta = now-then
print(delta.days)
print(delta.seconds)

# Number of days after date
def get_n_days_after_date(date_format="%d %b %Y", add_days=120):
    date_n_days_after = datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)
print(dt)

# n days before date:
def get_n_days_before_date(self, date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.datetime.now() - timedelta(days=days_before)
    return date_n_days_ago.strftime(date_format)

# Basic datetime objects usage
import datetime
# Date object
today = datetime.date.today()
new_year = datetime.date(2017, 1, 1)



# Current datetime
mow = datetime.datetime.now()

# Simple date arithmetic
import datetime
today = datetime.date.today()
print('Today:', today)
yesterday = today - datetime.timedelta(days=1)
print('yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tommorrow and yesterday;', tomorrow - yesterday)

# Converting timestamp to date
import time
from datetime import datetime
seconds_since_epoch=time.time()
utv_date=datetime.utcfromtimestamp(seconds_since_epoch)



# Subtracting months form a date using calender module.
import calendar
import calendar
from datetime import date
def mothdelta(data, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d, month=m, year=y)
import datetime
import dateutil.relativedelta

d = datetime.datetime.strptime("2013-03-31", "%Y-%m-%d")
d2 = d - dateutil.relativedelta.relativedelta(months=1)

print(str(datetime.datetime(2016, 7, 22, 9, 25, 59, 555555)))
from datetime import datetime
print(datetime.now().isoformat()) # get an ISO 8601 timestamps without timezone

from datetime import datetime
from dateutil.tz import tzlocal

print(datetime.now(tzlocal()).isoformat()) # ISO 8601 time stamps with time zone.

# Parsing a string with a short time zone name into timezone aware datetime object
from dateutil import tzfrom dateutil.parser import parse
ET = tz.gettz('US/Eastern')
CT = tz.gettz('US/Central')
MT = tz.gettz('US/Mountain')
PT = tz.gettz('US/Pacific')

us-tzfros = {'CST': CT, 'CDT': CT
             'EST': ET, 'EDT': ET,
             'MST': MT, 'MDT': MT,
             'PST': PT, 'PDT': PT}
dt_est = parse('2014-01-02 04:00:00 EST', tzinfos=us_tzinfos)
dt_pst = parse('2016-03-11 16:00:00 PST', tzinfos=us_tzinfos)
print(dt_est)

# Fuzzy datetime parsing
import datetime
# The size of each step in days
days_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
end_date = start_date + 7*days_delta

for i in range((end_date - start_date).days):
    print(start_date + i*days_delta)




