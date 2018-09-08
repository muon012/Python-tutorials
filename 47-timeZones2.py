print("---------------------------- 1 ----------------------------")
# Use the "awareLocalTime" variable to see how different the local time is from UTC time.
import datetime
import pytz

localTime = datetime.datetime.now()
utcTime = datetime.datetime.utcnow()

print("Naive local time: {}.".format(localTime))
print("Naive UTC time: {}.".format(utcTime))

awareLocalTime = pytz.utc.localize(utcTime).astimezone()
awareUtcTime = pytz.utc.localize(utcTime)

print("Aware local time is {} in time zone: {}.".format(awareLocalTime, awareLocalTime.tzinfo))
print("Aware UTC time is {} in time zone: {}.".format(awareUtcTime, awareUtcTime.tzinfo))

totoBday = datetime.datetime(2018, 3, 15, 15, 30, 6)
print(totoBday)