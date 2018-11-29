# If we try to access the time inside the database we will see that its type is of "str" and therefore we cannot
# use it if we want to change time zones. We can pass a parameter inside the "connect()" method that will turn the
# times into type datetime.datetime which can be converted to different time zones accordingly;

import sqlite3
import pytz

db = sqlite3.connect("84-accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
	utc_time = row[0]
	local_time = pytz.utc.localize(utc_time).astimezone()
	print("{}\t{}".format(utc_time, local_time))

db.close()